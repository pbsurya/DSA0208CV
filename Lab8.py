import cv2
from matplotlib import pyplot as plt

# Step 1: Read the image
image = cv2.imread('image5.png')  # Replace with your image path
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for matplotlib

# Step 2: Resize (scale) the image
# Scale down to half size
smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Scale up to double size
bigger = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_LINEAR)

# Step 3: Display all images
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Smaller (0.5x)")
plt.imshow(smaller)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Bigger (2x)")
plt.imshow(bigger)
plt.axis('off')

plt.tight_layout()
plt.show()
