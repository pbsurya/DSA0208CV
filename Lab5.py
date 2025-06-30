import cv2
import numpy as np
from matplotlib import pyplot as plt

# Step 1: Read the image
image = cv2.imread('image5.png', cv2.IMREAD_GRAYSCALE)  # Load in grayscale

# Step 2: Define kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Step 3: Apply erosion
eroded_image = cv2.erode(image, kernel, iterations=1)

# Step 4: Display original and eroded images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Eroded Image")
plt.imshow(eroded_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
