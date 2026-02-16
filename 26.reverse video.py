import cv2

cap = cv2.VideoCapture(r"C:\Users\Deepika\Desktop\MyProject\videoo.mp4")
frames = []

while True:
    ret, f = cap.read()
    if not ret: break
    frames.append(f)

cap.release()

h, w = frames[0].shape[:2]
out = cv2.VideoWriter("reverse.mp4",
                      cv2.VideoWriter_fourcc(*'mp4v'),
                      30, (w, h))

for f in frames[::-1]:
    out.write(f)
    cv2.imshow("Reverse", f)
    if cv2.waitKey(30) == 27: break   # press ESC to stop

out.release()
cv2.destroyAllWindows()
