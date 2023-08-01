# Video OCR Documentation

Video OCR (Optical Character Recognition) is a simple yet powerful tool that allows users to extract text from videos. It utilizes Tesseract OCR along with image processing techniques to recognize and retrieve textual content present in a video. The tool enables users to specify regions of interest (ROIs) containing text within the video frames, improving the accuracy and efficiency of the text extraction process.
The Video OCR tool is designed to handle a variety of text sizes, backgrounds, and text colors. It can be useful in scenarios where textual information needs to be extracted from video clips, presentations, lectures, tutorials, and more.
The Video OCR module is designed to extract text from videos and save the recognized text in a Word document. It offers a simple yet effective approach to perform Optical Character Recognition (OCR) on video frames. The module utilizes various libraries and custom functions to handle video processing, text recognition, and result generation.

## 2. Requirements
Before using the Video OCR tool, ensure that the following requirements are met:

Python 3.x
OpenCV (cv2) library
Pytesseract library
docx library
nltk library
Tesseract OCR (executable) installed on the system

## Mechanism Overview

The Video OCR module follows the following steps to process videos and extract text:

1. **Video Input:** The module takes a video file (e.g., `ala_neg.mp4`) as input, which contains the text that needs to be extracted.

2. **Region of Interest (ROI) Selection:** The user is prompted to select a region of interest (ROI) within the video frame. This ROI contains the text that will be processed for OCR.

3. **Image Preprocessing:** The selected ROI undergoes image preprocessing to enhance the text visibility and improve OCR accuracy. The preprocessing includes transformations like grayscale conversion and contrast enhancement.

4. **Text Detection and Recognition:** The preprocessed ROI is passed to the Tesseract OCR engine (using the `pytesseract` library) for text recognition. Tesseract performs OCR on the image and converts it into text.

5. **Text Scoring:** The recognized text is then scored based on the number of English words present in the text. The `nltk` library is used to tokenize the text and count the English words.

6. **Text Filtering and Optimization:** The module keeps track of the best-scoring text among consecutive frames to optimize the extracted text. If the score hasn't improved for a certain number of frames, the best result is appended to the list of recognized lines.

7. **Output to Word File:** Finally, the recognized text is saved to a Word document (`output.docx`) using the `python-docx` library.

## Library Usage

The Video OCR module relies on several libraries to achieve its functionalities. Here is a list of libraries used in this module:

### 1. `cv2` (OpenCV):

- OpenCV is a popular computer vision library used for video reading, frame manipulation, image preprocessing, and displaying the video frames.

### 2. `pytesseract`:

- `pytesseract` is a Python wrapper for the Tesseract OCR engine. It is used to perform OCR on the selected ROIs and extract text from images.

### 3. `python-docx`:

- The `python-docx` library is used to create a Word document and save the extracted text into it.

### 4. `nltk` (Natural Language Toolkit):

- The `nltk` library is used for text scoring based on the number of English words present in the recognized text.

### 5. `lighttransition`:

- `lighttransition` is a custom module containing image processing functions used for text detection. It includes functions to convert the image to grayscale and apply specific text enhancement techniques.

### 6. `selectinwindow`:

- `selectinwindow` is a custom module used to create a graphical user interface (GUI) window that allows the user to select the ROI by dragging the mouse over the video frame.

## Demo Video

To see the Video OCR module in action, please refer to the demo video ![video](https://drive.google.com/file/d/1xMxuxkkDsDvKT7VsMRuFhdbPG6h3yxvy/view?usp=drive_link).

## Usage

To use the Video OCR module, follow these steps:

1. Install the required libraries if you haven't already. You can install them using pip:

   ```
   pip install opencv-python pytesseract python-docx nltk
   ```

2. Download and install Tesseract OCR on your system. You can find the installation instructions [here](https://github.com/tesseract-ocr/tesseract).

3. Place the video file in place of (`ala_neg.mp4`) in the same directory as the `video_ocr.py` script.

4. Run the `video_ocr.py` script. The script will prompt you to specify the interval (in seconds) for video analysis and the text size category (very small, small, medium, large, very large).

5. The video window will appear, and you can drag your mouse to select the ROI containing the text you want to extract.

6. After selecting the ROI, the video processing will start, and you will see the processed frames with the text area highlighted.

7. Once the video processing is complete, the recognized text will be saved to a Word document (`output.docx`) in the same directory.

## Contributions

This Video OCR module is a simple implementation and works well with simple texts in videos. Contributors are welcome to improve the module's performance in various scenarios, including:

- Enhancing OCR accuracy for fast-moving texts
- Handling difficult backgrounds and text colors (e.g., bright and neon texts)
- Improving recognition of different font styles and handwriting

We encourage everyone to contribute and make this Video OCR module even more versatile and powerful.

## License

The Video OCR module and its associated files are released under the MIT License. You can find the full text of the license in the LICENSE file.

---

Thank you for using the Video OCR module! If you have any feedback or suggestions, please feel free to reach out to us. Happy text extraction from videos!

...
