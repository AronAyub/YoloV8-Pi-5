import cv2
print(cv2.__version__)

from ultralytics import YOLO
model = YOLO("yolov8n.pt")
model.predict(source=0, show=True)
#testing an image or video on local storage
#make sure it is in the same directory 
#model.predict(source="video_name.mp4", show=True)
##model.predict(source="image_name.jpg", show=True)
