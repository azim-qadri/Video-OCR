import cv2
import numpy as np

'''
Since this video Ocr is simple and works well with simple texts in videos.
You can contribute by making it work well with fast moving texts, difficult backgrounds and text colors such as too
bright and neon texts and different font styles ad handwriting.
All contributons are welcome
'''


def get_c_value(text_size):
    # Define the mapping between text size categories and c values
    c_values = {
        'very small': 45,
        'small': 40,
        'medium': 35,
        'large': 15,
        'very large': 10
    }

    # Return the corresponding c value based on the text size category
    return c_values.get(text_size.lower())


def black_text(image, cval):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray


def white_text(image, cval):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Convert grayscale image to BGR
    img_bgr = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    threshold_light_gray = 200  # Adjust this value as needed
    red_bgr = np.array([0, 0, 255])  # Remember, OpenCV uses BGR not RGB

    # Change all pixels that are lighter than the threshold in grayscale to red in BGR
    img_bgr[image > threshold_light_gray] = red_bgr

    # Create a mask for the red text
    red_mask = cv2.inRange(img_bgr, red_bgr, red_bgr)

    # Define a structuring element for the dilation (you can adjust the size as needed)
    se = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    # Dilate the red text
    dilated_mask = cv2.dilate(red_mask, se, iterations=1)

    # Create an empty color image
    result_img = np.zeros_like(img_bgr)

    # Use the dilated mask to put red text in the result image
    result_img[dilated_mask == 255] = red_bgr
    return result_img


def detectAndDisplay(frame):  # detection transformation
    text_cascade_name = r'C:\Users\User\AppData\Local\Programs\Python\Python311\Lib\site-packages\cv2\data\haarcascade_licence_plate_rus_16stages.xml'
    text_cascade = cv2.CascadeClassifier()
    text_cascade.load(filename=text_cascade_name)
    frame_gray = cv2.equalizeHist(frame)
    # -- Detect faces
    texts = text_cascade.detectMultiScale3(frame_gray)
    return texts

