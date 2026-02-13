import cv2
import numpy as np

# Read image
img = cv2.imread("flower.png")
orig = img.copy()  # Keep a copy of original

# Crop ROI (example)
roi = img[50:113, 100:126]  # y1:y2, x1:x2

# Target position
x, y = 50, 200

# Compute max height and width to avoid going out of image
h, w = img.shape[:2]
th = min(roi.shape[0], h - y)
tw = min(roi.shape[1], w - x)

# Paste ROI safely
img[y:y+th, x:x+tw] = roi[:th, :tw]

# Show original and modified images
cv2.imshow("Original Image", orig)
cv2.imshow("ROI Cropped & Pasted", img)
cv2.imwrite("roi_image.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
