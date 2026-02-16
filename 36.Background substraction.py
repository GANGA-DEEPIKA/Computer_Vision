import cv2, numpy as np

img = cv2.imread("flower.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv, (35,50,50), (85,255,255))
res = cv2.bitwise_and(img, img, mask=~mask)
cv2.imshow("original",img)
cv2.imshow("Result", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
