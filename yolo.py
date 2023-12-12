from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt")

results = model(source='peningkatan-kendaraan-keluar-jakarta-2.jpeg',show=True,conf=0.4,save=True)
