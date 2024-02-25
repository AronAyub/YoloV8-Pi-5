import cv2
print(cv2.__version__)

from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.predict(source=0, show=True)