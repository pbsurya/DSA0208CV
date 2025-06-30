import cv2
import numpy as np

# Step 1: Read the image in grayscale
img = cv2.imread('image6.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found.")
    exit()

# Step 2: Define Laplacian kernel with a negative center
laplacian_kernel = np.array([[0,  1, 0],
                             [1, -4, 1],
                             [0,  1, 0]])

# Step 3: Apply the Laplacian filter
laplacian = cv2.filter2D(img, cv2.CV_64F, laplacian_kernel)

# Step 4: Sharpen the image by subtracting the Laplacian
sharpened = cv2.convertScaleAbs(img - laplacian)

# Step 5: Show the result
cv2.imshow('Original Image', img)
cv2.imshow('Sharpened Image (Laplacian - Negative Center)', sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
