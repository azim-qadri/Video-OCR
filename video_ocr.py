import cv2
import pytesseract
from docx import Document
import sys
import selectinwindow
import pyautogui
import time
import lighttransition
from nltk.corpus import words
from nltk.tokenize import word_tokenize

# Prepare a set of English words
english_words = set(words.words())


# Scoring function
def score_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Count the number of English words
    english_word_count = sum(1 for t in tokens if t in english_words)

    # Return the score
    return english_word_count / len(tokens) if tokens else 0


def select_region(path):
    video = cv2.VideoCapture(path)
    coors = None
    # Set the position to the fifth frame
    frame_number = 0  # Zero-based index, so the 20th frame is at index 19th
    video.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    # Set recursion limit
    sys.setrecursionlimit(10 ** 9)

    # Initialize the drag object
    screen_width, screen_height = pyautogui.size()
    wName = "select region"
    imageWidth = int(screen_width * 3 / 4)
    imageHeight = int(screen_height * 3 / 4)
    while(video):
        # Read the frame
        ret, frame = video.read()
        if not ret:
            break
        frame = cv2.copyMakeBorder(frame, 20, 20, 20, 20, cv2.BORDER_CONSTANT, value=1)
        # Display the image
        cv2.imshow(wName, frame)
        # Define the drag object
        rectI = selectinwindow.DragRectangle(frame, wName, imageWidth, imageHeight)
        cv2.setMouseCallback(rectI.wname, selectinwindow.dragrect, rectI)
        key = cv2.waitKey(3) & 0xFF
        # If returnflag is True, break from the loop
        if rectI.returnflag:
            coors = rectI.outRect
            # Close all open windows
            video.release()
            cv2.destroyAllWindows()
            break
        if key == ord('s'):
            break
    return coors


def extract_frames(video_path, frame_rate, cat):
    rect = select_region(video_path)
    x, y, width, height = rect.x, rect.y, rect.w, rect.h
    video_capture = cv2.VideoCapture(video_path)
    frame_counter = 0
    last_text = None
    recognized_lines = []
    best_score = 0
    best_result = ''
    no_improve_counter = 0

    while True*2:
        ret, frame = video_capture.read()
        if not ret:
            break
        if ret:
            try:
                if frame_counter % frame_rate == 0 and frame_rate != 0:
                    # Crop the frame to the selected rectangle
                    frame = frame[y:y + height, x:x + width]
                    cval = lighttransition.get_c_value(cat)
                    frame = lighttransition.black_text(frame, cval)  # OpenCv transitions or other transitions improving the frames for ocr can be applied
                    cv2.imshow('Text Area', frame)
                    # Perform OCR on the cropped image
                    custom_config = r'--psm 6 --oem 1'
                    text = pytesseract.image_to_string(frame, lang='eng', config=custom_config)
                    score = score_text(text)
                    if score > best_score:
                        # If the score is better, update the best result and reset the counter
                        best_score = score
                        best_result = text
                        no_improve_counter = 0
                    else:
                        # If the score hasn't improved, increment the counter
                        no_improve_counter += 1

                    if no_improve_counter >= 10:
                        # If the score hasn't improved for 10 iterations, append the best result to the list
                        if last_text != best_result:
                            recognized_lines.append(best_result)
                            last_text = best_result
                            print(best_result)

                        # Reset the best result and score
                        best_score = 0
                        best_result = ''
                        no_improve_counter = 0

            except cv2.error as e:
                print(e)
                break

        if cv2.waitKey(1) == ord('q'):
            break

        frame_counter += 1
    video_capture.release()
    cv2.destroyAllWindows()
    return recognized_lines


def save_to_word_file(texts, output_file):
    doc = Document()
    for text in texts:
        doc.add_paragraph(text)
    doc.save(output_file)


def main():
    # Set the path to the Tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Programs\Tesseract-OCR\tesseract.exe' # Loaction to your tesseract.exe file in your system after installing tesseract ocr

    start = time.time()
    video_path = "ala neg.mp4"  # Enter your video path here
    output_file = "output.docx"  # Enter your word file name here
    frame_rate = int(input("Specify the interval (in seconds) for video analysis: "))*3/4  #Enter process rate-less rate more accurate
    text_size_category = input("Enter the text size category (very small, small, medium, large, very large): ")  # Size of the text in the video
    frames = extract_frames(video_path, frame_rate, text_size_category)
    save_to_word_file(frames, output_file)

    end = time.time()
    print('Elapsed time:', end - start)


if __name__ == '__main__':
    main()
