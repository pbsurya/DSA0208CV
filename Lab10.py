import cv2
import numpy as np
from matplotlib import pyplot as plt

# Step 1: Read the image
image = cv2.imread("image5.png")  # Update with your correct image path

if image is None:
    print("Error: Image not found.")
    exit()

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Step 2: Define translation matrix (move right by 100px and down by 50px)
rows, cols = image.shape[:2]
translation_matrix = np.float32([[1, 0, 100], [0, 1, 50]])

# Step 3: Apply the translation
moved_image = cv2.warpAffine(image, translation_matrix, (cols + 100, rows + 50))

# Step 4: Display original and moved images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Moved Image")
plt.imshow(moved_image)
plt.axis('off')

plt.tight_layout()
plt.show()
