import cv2

# Step 1: Open the video file or camera
video_path = 'video1.mp4'  # Replace with 0 for webcam
cap = cv2.VideoCapture(video_path)

# Function to play video with given speed
def play_video(speed_delay, title):
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart video
    print(f"Playing video: {title}")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow(title, frame)
        if cv2.waitKey(speed_delay) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()

# Step 2: Display video in normal speed (delay ~25ms)
play_video(speed_delay=25, title="Normal Speed")

# Step 3: Display video in slow motion (delay ~100ms)
play_video(speed_delay=100, title="Slow Motion")

# Step 4: Display video in fast motion (delay ~5ms)
play_video(speed_delay=5, title="Fast Motion")

# Release the video capture
cap.release()
cv2.destroyAllWindows()
