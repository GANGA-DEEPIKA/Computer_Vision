import cv2, numpy as np

w, h = map(int, input("Enter Width Height: ").split())
img = np.ones((h, w, 3), np.uint8) * 255

# Draw rectangle (start point, end point, color, thickness)
cv2.rectangle(img, (w//4, h//4), (3*w//4, 3*h//4), (0, 0, 255), 3)

cv2.imshow("Rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
