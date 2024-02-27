# Blueprint-Co-Challenge

This repository contains a Python script which makes use of OpenCV to compare two PDF documents based on their visual content. It aims to detect and highlight differences between the layouts in the PDFs.

#Approach:

PDF to Image Conversion: 
The script utilizes the pdf2image library to efficiently convert both input PDFs (file_1.pdf and file_2.pdf) into corresponding images.

Image Comparison:
The script uses cv2.absdiff() function from OpenCV. This calculates the absolute difference between corresponding elements of two input arrays (typically images). This function detects the changes between images, highlighting areas of significant pixel intensity variation.
Along with this function thresholding is applied to the difference image to control the sensitivity of change detected. In the script cv2.THRESH_BINARY is used.

Highlighting the change: 
These difference areas are highlighted using a colored overlay on the common mask of the two input images.

#Detailed Instructions for Using the Code:

1.Prerequisites:
OpenCV installation: Install OpenCV using pip:
  pip install opencv-python
pdf2image installation: Install the pdf2image library for PDF conversion:
  pip install pdf2image
  **make sure the to download poppler and set it in path for the pdfinfo module to work.
2.Downloading the Code:
Download the Python script "" from the GitHub repository.
3.Placing your PDF Files:
Place the two PDF documents (file_1.pdf and file_2.pdf)you want to compare in the same directory as your Python script.
4.Interpreting the Results:
The script will generate an output file named output.pdf. This image will be a copy of the first PDF (file_1.pdf) with areas of significant difference highlighted using a colored overlay.
**make sure to give path for the PDF file generated.


#Expected Output:

The output.pdf file will be an image of the first PDF (file_1.pdf) with visually significant differences highlighted using a specific color overlay. Red colour is highlighting the differences of file_1 and blue colour highlighting differences of file_2. This allows for easy identification of discrepancies between the two documents.


