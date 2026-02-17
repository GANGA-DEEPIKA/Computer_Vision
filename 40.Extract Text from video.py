import cv2
import pytesseract

# If needed, set Tesseract path (Windows only)
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        text = pytesseract.image_to_string(frame)
        print(text)

    cap.release()

# Call function
extract_text("vehiclevideo.mp4")
