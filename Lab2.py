import cv2
from matplotlib import pyplot as plt

# Step 1: Read the image
image = cv2.imread('image2.png')  # Replace with your image file name

# Step 2: Apply Gaussian Blur
blurred_image = cv2.GaussianBlur(image, (7, 7), 0)  # (7,7) is the kernel size

# Step 3: Display original and blurred images
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Gaussian Blurred Image')
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.show()
