import cv2

cap = cv2.VideoCapture("vehiclevideo.mp4")
frames = []

# Store all frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Play in reverse (slow motion)
for f in reversed(frames):
    cv2.imshow("Reverse Slow Video", f)
    if cv2.waitKey(60) & 0xFF == ord('q'):  # 60 ms delay = slow motion
        break

cv2.destroyAllWindows()
