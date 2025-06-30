import cv2
from matplotlib import pyplot as plt

# Step 1: Read the image
image = cv2.imread("image5.png")  # Update path

if image is None:
    print("Error: Image not found. Check the file path.")
    exit()

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # For matplotlib display

# Step 2: Rotate the image
# 90 degrees clockwise
clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# 90 degrees counter-clockwise
counter_clockwise = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Step 3: Display all images
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Clockwise Rotation")
plt.imshow(clockwise)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Counter-Clockwise Rotation")
plt.imshow(counter_clockwise)
plt.axis('off')

plt.tight_layout()
plt.show()
