import cv2
import numpy as np

# Load the image
img = cv2.imread("flower.png", 0)  

# Define a kernel (structuring element)
kernel = np.ones((5,5), np.uint8)

# Apply Erosion
erosion = cv2.erode(img, kernel, iterations=1)

# Show images
cv2.imshow("Original", img)
cv2.imshow("Erosion", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
