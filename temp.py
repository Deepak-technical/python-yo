import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Get the width and height of the video frame
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Print the width and height of the video frame
print("Frame width:", frame_width)
print("Frame height:", frame_height)

# Release the VideoCapture object
cap.release()