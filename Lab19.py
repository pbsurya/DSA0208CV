import cv2
import numpy as np

# Step 1: Read the image in grayscale
img = cv2.imread('image6.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found.")
    exit()

# Step 2: Apply Sobel operator along X and Y axes
sobel_x = cv2.Sobel(img, cv2.CV_64F, dx=1, dy=0, ksize=3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, dx=0, dy=1, ksize=3)

# Step 3: Combine the two gradients (magnitude)
sobel_xy = cv2.magnitude(sobel_x, sobel_y)

# Step 4: Convert to 8-bit image
sobel_xy_abs = cv2.convertScaleAbs(sobel_xy)

# Step 5: Show the result
cv2.imshow('Original Image', img)
cv2.imshow('Sobel XY Edge Detection', sobel_xy_abs)
cv2.waitKey(0)
cv2.destroyAllWindows()
