import cv2
import numpy as np

img = cv2.imread("flower.png")
rows, cols = img.shape[:2]

# 4 points from original image
pts1 = np.float32([[50,50], [200,50], [50,200], [200,200]])

# 4 new points (destination)
pts2 = np.float32([[10,100], [220,50], [100,250], [250,220]])

# Get perspective transform matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply transformation
result = cv2.warpPerspective(img, M, (cols, rows))

cv2.imshow("Original", img)
cv2.imshow("Perspective Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
