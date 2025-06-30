import cv2
import numpy as np

# Step 1: Read the image in grayscale
img = cv2.imread('image6.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found.")
    exit()

# Step 2: Apply Sobel operator along the X-axis
sobel_x = cv2.Sobel(img, cv2.CV_64F, dx=1, dy=0, ksize=3)

# Step 3: Convert the result to uint8 for display
sobel_x_abs = cv2.convertScaleAbs(sobel_x)

# Step 4: Show the result
cv2.imshow('Original Image', img)
cv2.imshow('Sobel X Edge Detection', sobel_x_abs)
cv2.waitKey(0)
cv2.destroyAllWindows()
