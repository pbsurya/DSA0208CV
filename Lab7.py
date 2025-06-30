import cv2

# Open webcam (use 0 for default camera)
cap = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

def display_video(title, delay):
    print(f"Showing video: {title} (Press 'q' to exit)")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow(title, frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

# Normal speed (approx 30 FPS → ~33ms delay)
display_video("Normal Speed", delay=33)

# Slow motion (lower FPS → ~150ms delay)
display_video("Slow Motion", delay=150)

# Fast motion (higher FPS → ~5ms delay)
display_video("Fast Motion", delay=5)

# Release the webcam
cap.release()
cv2.destroyAllWindows()
