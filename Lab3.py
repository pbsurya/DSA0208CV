import cv2
from matplotlib import pyplot as plt

# Step 1: Read the image
image = cv2.imread('image3.png')  # Replace with your actual image file name

# Step 2: Convert to grayscale (Canny works on single channel images)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Canny edge detection
edges = cv2.Canny(gray_image, threshold1=100, threshold2=200)

# Step 4: Display original and edge-detected images
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Canny Edge Detection')
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.show()
