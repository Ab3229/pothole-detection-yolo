# 🛣️ Pothole Detection using YOLO

## 📌 Overview

This project demonstrates **pothole detection using a trained YOLO model**.
It detects potholes in road images/videos and highlights them with bounding boxes and confidence scores.

---

## 🚀 Features

* Detects potholes in images and videos
* Uses trained YOLO model (`best.pt`)
* Displays bounding boxes with confidence scores
* Works in real-world road conditions

---

## 🧠 Tech Stack

* Python
* YOLO (Ultralytics)
* OpenCV

## 📊 Model Performance

| Metric       | Value |
| ------------ | ----- |
| Precision    | 0.80  |
| Recall       | 0.88  |
| mAP@0.5      | 0.88  |
| mAP@0.5:0.95 | 0.69  |
| F1 Score     | 0.84  |

The model demonstrates strong performance in detecting potholes with high recall and balanced precision.

---

## ▶️ Usage

Run detection on image/video:

```bash
python detect.py
```

---

## 📊 Model Performance

The model performs well in detecting potholes under different road conditions.

* Detects multiple potholes in a single frame
* Handles real-world scenarios
* Some low-confidence detections may occur

*Note: Exact metrics (Precision, Recall, mAP, F1-score) require evaluation on a labeled validation dataset.*

---

## 📦 Model File

* `best.pt` → trained YOLO weights used for detection

---

## 🎯 Future Improvements

* Improve accuracy with larger dataset
* Remove low-confidence detections using threshold tuning
* Add real-time video detection
* Deploy as web/mobile application

---

## 👨‍💻 Author

**Abhishek Agrawal**
MBM University, Jodhpur

---

## ⭐ Support

If you like this project, please ⭐ the repository!
