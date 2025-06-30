import cv2
import numpy as np

# Step 1: Read the image in grayscale
img = cv2.imread('image6.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found.")
    exit()

# Step 2: Apply Sobel operator along the Y-axis
sobel_y = cv2.Sobel(img, cv2.CV_64F, dx=0, dy=1, ksize=3)

# Step 3: Convert the result to uint8 for display
sobel_y_abs = cv2.convertScaleAbs(sobel_y)

# Step 4: Show the result
cv2.imshow('Original Image', img)
cv2.imshow('Sobel Y Edge Detection', sobel_y_abs)
cv2.waitKey(0)
cv2.destroyAllWindows()
