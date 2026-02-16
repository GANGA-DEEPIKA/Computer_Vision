import cv2

img = cv2.imread("V.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = cv2.CascadeClassifier(cv2.data.haarcascades +
                             "haarcascade_frontalface_default.xml")

eye = cv2.CascadeClassifier(cv2.data.haarcascades +
                            "haarcascade_eye_tree_eyeglasses.xml")

faces = face.detectMultiScale(gray, 1.1, 5)

for (x,y,w,h) in faces:
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    eyes = eye.detectMultiScale(
        roi_gray,
        scaleFactor=1.1,
        minNeighbors=8,      # increased for accuracy
        minSize=(30,30)      # ignore tiny false detections
    )

    for (ex,ey,ew,eh) in eyes[:2]:
        cv2.rectangle(roi_color,(ex,ey),
                      (ex+ew,ey+eh),(255,0,0),2)

cv2.imshow("Eye Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
