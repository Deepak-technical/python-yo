from ultralytics import YOLO
import cv2
import cvzone
import math

WINDOW_NAME = 'Full Integration'

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
# cap = cv2.VideoCapture('./video3.mp4')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1980)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
# cap.set(cv2.CAP_PROP_AUTOFOCUS, 6)
cap.set(cv2.CAP_PROP_FPS, 120)
model = YOLO("./YOLO8_weights/yolo_nano_small.pt")

classNames = ['missing', 'overlaps']
myColor = (0, 0, 0)

while cap.isOpened():
    success, img = cap.read()
    results = model(img, stream=True)
    
    for r in results:
        boxes = r.boxes
        
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            
            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])
            currentClass = classNames[cls]
            
            if (conf>0.20 and currentClass=='missing') or (conf>0.35 and currentClass=='overlaps') :
                if currentClass == 'missing':
                    myColor = (0,0,255)
                else:
                    myColor = (18, 191, 41)
                
                img = cvzone.cornerRect(
                img,  # The image to draw on
                (x1,y1,w,h),  # The position and dimensions of the rectangle (x, y, width, height)
                l=1,  # Length of the corner edges
                t=2,  # Thickness of the corner edges
                rt=2,  # Thickness of the rectangle
                colorR=myColor,  # Color of the rectangle
                colorC=myColor  # Color of the corner edges
            )

    cv2.imshow("Image", img)
    cv2.waitKey(1)
