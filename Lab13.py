import cv2
import numpy as np

cap = cv2.VideoCapture('video1.mp4')

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

pts1 = np.float32([[100, 100], [400, 100], [100, 400], [400, 400]])
pts2 = np.float32([[150, 150], [350, 100], [130, 380], [370, 420]])
M = cv2.getPerspectiveTransform(pts1, pts2)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    warped = cv2.warpPerspective(frame, M, (frame.shape[1], frame.shape[0]))
    cv2.imshow('Perspective Video', warped)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
