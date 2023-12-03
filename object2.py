from ultralytics import YOLO
import cv2
import cvzone
import math

WINDOW_NAME = 'Full Integration'

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 560)
model = YOLO("./yolo_nano_small.pt")

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
            
            if currentClass == 'missing':
                myColor = (0,0,255)
            else:
                myColor = (18, 191, 41)
            
            cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 3)
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}',
                               (max(0, x1), max(35, y1)), scale=1.3, thickness=2, colorB=myColor,
                               colorT=(255, 255, 255), colorR=myColor, offset=5)
            cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 1)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
