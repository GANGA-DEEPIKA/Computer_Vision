import cv2, numpy as np

text = input("Enter text: ")
img = np.ones((400, 600, 3), np.uint8) * 255

cv2.putText(img, text, (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

cv2.imshow("Text Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
