import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('image4.png', cv2.IMREAD_GRAYSCALE)
kernel = np.ones((5, 5), np.uint8)  # Corrected this line
dilated_image = cv2.dilate(image, kernel, iterations=1)

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('Dilated Image')
plt.imshow(dilated_image, cmap='gray')
plt.show()
