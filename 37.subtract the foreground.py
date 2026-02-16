import cv2, numpy as np

img = cv2.imread("flower.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Example: remove red foreground
lower = np.array([0,120,70])
upper = np.array([10,255,255])

mask = cv2.inRange(hsv, lower, upper)
result = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

cv2.imshow("Input Image", img)
cv2.imshow("Foreground Removed", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
