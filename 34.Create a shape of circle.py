import cv2, numpy as np

w, h = map(int, input("Enter Width Height: ").split())
img = np.ones((h, w, 3), np.uint8) * 255

cv2.circle(img, (w//2, h//2), min(w,h)//4, (255,0,0), 3)

cv2.imshow("Circle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
