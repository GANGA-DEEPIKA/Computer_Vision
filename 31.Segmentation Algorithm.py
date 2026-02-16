import cv2

# Read image in grayscale
img = cv2.imread("flower.png")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# Apply threshold (change 127 to your threshold value)
_, segmented = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Show result
cv2.imshow("original image",img)
cv2.imshow("Segmented Image", segmented)
cv2.waitKey(0)
cv2.destroyAllWindows()
