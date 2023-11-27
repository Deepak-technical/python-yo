from ultralytics import YOLO

model=YOLO("./bestWeights.pt")
model.predict(source="0",show=True,conf=0.3)