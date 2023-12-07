import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Get the width and height of the video frame
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# cap.set(cv2.CAP_PROP_AUTOFOCUS, 6)
cap.set(cv2.CAP_PROP_FPS, 60)

# Get the width and height of the video frame
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_fps = cap.get(cv2.CAP_PROP_FPS)


print("Frame width:", frame_width)
print("Frame height:", frame_height)
print("Frame height:", frame_fps)

# Release the VideoCapture object
cap.release()