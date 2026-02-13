import cv2
image = cv2.imread("flower.png")
watermark_text = "My Watermark"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, watermark_text, (1, 50),
            font, 1, (0, 0, 250), 2, cv2.LINE_AA)
cv2.imwrite("watermarked.jpg", image)

cv2.imshow("Watermarked Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
