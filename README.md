Your README is already solid 👍 — I’ll refine it into a **clean, professional GitHub-ready version** with better structure, clarity, and links properly embedded.

---

# 🛣️ Pothole Detection using YOLO

## 📌 Overview

This project demonstrates **pothole detection using a trained YOLO model**.
It identifies potholes in road images and videos, drawing bounding boxes along with confidence scores.

The system is designed to work in **real-world road conditions**, making it useful for smart transportation and road safety applications.

---

## 🚀 Features

* Detects potholes in **images and videos**
* Uses a trained YOLO model (`best.pt`)
* Displays **bounding boxes with confidence scores**
* Handles **multiple potholes in a single frame**
* Works in **real-world scenarios**

---

## 🧠 Tech Stack

* **Python**
* **YOLO (Ultralytics)**
* **OpenCV**

---

## 📊 Model Performance

| Metric       | Value |
| ------------ | ----- |
| Precision    | 0.80  |
| Recall       | 0.88  |
| mAP@0.5      | 0.88  |
| mAP@0.5:0.95 | 0.69  |
| F1 Score     | 0.84  |

The model achieves **high recall (0.88)**, meaning it successfully detects most potholes, while maintaining a good balance with precision.

---

## 🎥 Results

### 📥 Input Video

👉 [Click to View Input Video](https://drive.google.com/file/d/1-ClzcldjV30NuBKYQXtmmIOIW5O-JRFS/view?usp=sharing)

### 📤 Output Video (Detection)

👉 [Click to View Output Video](https://drive.google.com/file/d/1LB5yWtyz-Ny8rperV2Io8Jl9xo2H8vmq/view?usp=sharing)

---

## ▶️ Usage

Run detection on image/video:

```bash
python detect.py
```

---

## 📦 Model File

* `best.pt` → Trained YOLO weights used for detection

---

## ⚙️ How It Works

1. Input image/video is passed to the YOLO model
2. Model predicts pothole locations
3. Bounding boxes are drawn with confidence scores
4. Output video/image is generated

---

## 🎯 Future Improvements

* Improve accuracy with a **larger and more diverse dataset**
* Apply **confidence threshold tuning** to reduce false detections
* Implement **real-time detection (live camera)**
* Deploy as a **web or mobile application**
* Add **GPS tagging for pothole mapping**

---

## 👨‍💻 Author

**Abhishek Agrawal**
MBM University, Jodhpur

🔗 GitHub: [https://github.com/Ab3229](https://github.com/Ab3229)

---

## ⭐ Support

If you like this project, please ⭐ the repository and share it!


