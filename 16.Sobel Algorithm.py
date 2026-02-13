import cv2

# Read original image
img = cv2.imread("flower.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel X, Y and combined
sx = cv2.convertScaleAbs(cv2.Sobel(gray, cv2.CV_64F, 1, 0, 3))
sy = cv2.convertScaleAbs(cv2.Sobel(gray, cv2.CV_64F, 0, 1, 3))
sc = cv2.addWeighted(sx, 0.5, sy, 0.5, 0)

# Display all images
for name, im in zip(["Original", "Sobel X","Sobel Y","Combined"], [img, sx, sy, sc]):
    cv2.imshow(name, im)
    cv2.imwrite(name.replace(" ","_")+".jpg", im)

cv2.waitKey(0)
cv2.destroyAllWindows()
