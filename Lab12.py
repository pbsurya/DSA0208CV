import cv2
import numpy as np
img = cv2.imread('image6.png')
rows, cols = img.shape[:2]
pts1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1], [cols - 1, rows - 1]])
pts2 = np.float32([[50, 50], [cols - 50, 30], [70, rows - 50], [cols - 50, rows - 30]])
# Perspective matrix
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (cols, rows))
cv2.imwrite('perspective_image.jpg', dst)