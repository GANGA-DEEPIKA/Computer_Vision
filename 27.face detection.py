import cv2

img = cv2.imread("virat.png")
img = cv2.resize(img, (400,200))   # resize fix
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = cv2.CascadeClassifier(cv2.data.haarcascades +
                             "haarcascade_frontalface_default.xml")

for x,y,w,h in face.detectMultiScale(gray,1.1,4):
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Face", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
