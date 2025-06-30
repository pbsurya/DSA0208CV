import cv2
import numpy as np
from matplotlib import pyplot as plt

def display(img, title):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

# Load image
image = cv2.imread(r'C:\Users\Surya\OneDrive\Pictures\Totoro.jpg')  # Replace with your image path
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel_pos_center = np.array([[ 0, -1,  0],
                              [-1,  5, -1],
                              [ 0, -1,  0]])

sharpened_pos = cv2.filter2D(gray, -1, kernel_pos_center)
display(sharpened_pos, 'Sharpened - Positive Center Laplacian') 
