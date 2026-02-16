import cv2
import numpy as np

size = int(input("Enter size: "))

# White image
img = np.ones((size, size, 3), np.uint8) * 255

b = size // 10   # box size

# 4 corner boxes
img[0:b, 0:b] = (0,0,0)              # Black
img[0:b, size-b:size] = (255,0,0)    # Blue
img[size-b:size, 0:b] = (0,255,0)    # Green
img[size-b:size, size-b:size] = (0,0,255)  # Red

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
