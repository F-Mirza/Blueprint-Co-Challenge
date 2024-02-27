import numpy as np
import pdf2image
import cv2 #OpenCV library for python
import img2pdf
from PIL import Image

def pdf_to_image(pdf_path, dpi=51,output_path=None):
  # Convert PDF to images using pdf2image
  images = pdf2image.convert_from_path(pdf_path, dpi=dpi,poppler_path=r'C:\Program Files\Release-24.02.0-0\poppler-24.02.0\Library\bin')
  #the image obtained in PIL format
  image = images[0]
  # Convert PIL image to OpenCV format
  opencv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

  #if you want to store images locally as well
  cv2.imwrite(output_path, opencv_image)

  return opencv_image


# taking files: file_.pdf and file_2.pdf as inputs, saving them is optional
image1 = pdf_to_image('file_1.pdf',output_path="fil1.jpg")
image2 = pdf_to_image('file_2.pdf',output_path="fil2.jpg")


cv2.imshow("image 1",image1)
cv2.imshow("image 2",image2)

#converting them into grayscale
gry1=cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
gry2=cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)

#absolute difference
diff1=cv2.absdiff(gry1,gry2)
#thresholding
_, thresh = cv2.threshold(diff1, 56, 255, cv2.THRESH_BINARY)  # Adjust threshold if needed
mask1 = cv2.bitwise_not(thresh)#swap the binary values
mask = cv2.cvtColor(mask1, cv2.COLOR_GRAY2BGR)#converting into BGR iamge for further processing

#creating empty arrays of the image size
red_diff = np.zeros_like(image1)
blue_diff = np.zeros_like(image2)

red_diff[gry1 == 0] = [255, 255, 255]   # red for differences in img1
blue_diff[gry2 == 0] = [255, 255, 255]    # blue for differences in img2

# Create a mask to identify the overlapping regions
overlap_mask = cv2.bitwise_and(red_diff, blue_diff)
red_diff[gry1 == 0] = [0, 0, 255] 
blue_diff[gry2 == 0] = [255, 0, 0]  
overlap_color = [0, 255, 0] 
final_diff = cv2.addWeighted(image1, 1, red_diff, 10, 0)#overlaying  red_diff on the image1
no_overlap_mask = cv2.bitwise_not(overlap_mask)

# Blend the modified final difference mask with blue differences
ff = cv2.addWeighted(final_diff, 0.6, blue_diff, 1, 0)
ff[overlap_mask != 0] = image1[overlap_mask != 0]

#view final output
cv2.imshow("output",ff)
cv2.imwrite("output.jpg", ff)

cv2.waitKey(0)
cv2.destroyAllWindows()


def img_to_pdf(image):
    # converting into chunks using img2pdf
    image = Image.fromarray(image)#convert to PIL image
    pdf_bytes = img2pdf.convert(image)

    # opening or creating pdf file
    file = open(r"C:\Users\fizza\OneDrive\Desktop\internship_cv", "wb")

    # writing pdf files with chunks
    file.write(pdf_bytes)

    # closing image file and pdf file
    image.close()
    file.close()
    # prints
    print("Successfully generated output pdf file")



#to convert final output image into pdf
img_to_pdf(ff)
