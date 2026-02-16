import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread("flower.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Create kernel
kernel = np.ones((5,5), np.uint8)

# Opening = Erosion followed by Dilation
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)

# Show result
cv2.imshow("Original", img)
cv2.imshow("Opening", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()
