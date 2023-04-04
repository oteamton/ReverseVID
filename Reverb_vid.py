import cv2

# Create a VideoCapture object to capture video from the default camera
cap = cv2.VideoCapture("D:\\Space\\poe_vids\\Path of Exile 2023.02.20 - 11.36.42.03.DVR.mp4")

# Check if the camera was successfully opened
if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

# Get the frame rate of the original video
fps = int(cap.get(cv2.CAP_PROP_FPS))
print("Frame rate:", fps)

# Get the total number of frames in the video
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Start at the last frame
cap.set(cv2.CAP_PROP_POS_FRAMES, num_frames - 1)

# Loop through the frames from the camera in reverse order
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        print("Error: Could not read frame")
        break

    # Display the frame
    cv2.imshow('Video', frame)

    # Move to the previous frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, cap.get(cv2.CAP_PROP_POS_FRAMES) - 1)

    # Wait for a key press to exit
    if cv2.waitKey(int(1000/fps)) == ord('q'):  # add delay based on original video frame rate
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()
