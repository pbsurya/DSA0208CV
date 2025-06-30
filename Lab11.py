import cv2
import numpy as np
img = cv2.imread('image6.png')
rows, cols = img.shape[:2]
# Source and destination points
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
# Affine transform matrix
M = cv2.getAffineTransform(pts1, pts2)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imwrite('affine_output.jpg', dst)