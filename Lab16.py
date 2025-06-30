import cv2

# Step 1: Read the image in grayscale
img = cv2.imread('image6.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found.")
    exit()

# Step 2: Apply Canny edge detection
edges = cv2.Canny(img, threshold1=100, threshold2=200)

# Step 3: Show the original and edge-detected images
cv2.imshow('Original Image', img)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
