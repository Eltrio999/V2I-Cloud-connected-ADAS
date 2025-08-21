# 🚗 Cloud-Connected Driver Notification System

An intelligent real-time driver assistance system that leverages GPS, cloud analytics (AWS), and AI-powered traffic sign recognition to notify drivers of current road conditions—even without internet access.

---

## 📘 Project Overview

Modern roads often present unpredictable challenges like accidents, construction, or weather changes. This project offers a hybrid system combining AWS-based cloud processing and on-device AI to alert drivers of such conditions in real-time, ensuring greater safety and driving efficiency.

---

## 📌 Features

- 📍 Live GPS tracking via Neo-6M module  
- ☁️ Cloud integration using AWS and Google Maps  
- 📱 Real-time road alerts through Blynk mobile app  
- 🧠 On-device traffic sign detection using YOLOv8  
- 🤖 Chatbot interface for driver queries (planned)  
- 🛠️ Modular architecture for easy upgrades

---

## 🔧 Hardware and Software Components

| Component                | Description                                      |
|--------------------------|--------------------------------------------------|
| Raspberry Pi 3B+         | Main processing and communication hub           |
| Neo-6M GPS Module        | Provides real-time latitude & longitude         |
| Raspberry Pi Camera v1.3 | Captures live road footage                      |
| AWS IoT + AWS Lambda     | Cloud services for data processing              |
| Google Maps API          | GPS coordinate visualization                    |
| Blynk                    | Delivers alerts to the driver's mobile device   |
| YOLOv8                   | AI model for traffic sign classification        |
| Python, PyTorch, OpenCV  | Framework and libraries for processing and AI   |

---

## 🔄 System Workflow

1. GPS module gathers real-time coordinates  
2. Raspberry Pi sends data to AWS IoT Core  
3. AWS Lambda processes and stores data, updates Google Maps  
4. Blynk app notifies drivers of upcoming road conditions  
5. YOLOv8 runs locally to detect traffic signs even when AWS is unreachable

---

## 🤖 AI Traffic Sign Recognition

- Trained using pre-annotated traffic sign dataset  
- Deployed locally on Raspberry Pi using PyTorch + OpenCV  
- Real-time classification from live camera feed  
- Operates independently of cloud connectivity  

---

## 📊 Results and Testing

- ✅ Precision, confidence & recall curves analyzed  
- ✅ Confusion matrix evaluated for model accuracy  
- ✅ YOLOv8 tested successfully on live video input  
- ✅ Real-time location confirmed on AWS & Blynk dashboards  
- ✅ Fully functional prototype implemented and tested  

---

## 💡 Benefits

- Increases road safety with proactive alerts  
- Dual-mode: cloud-enabled with offline AI fallback  
- Minimizes fuel consumption and travel delays  
- Modular and scalable for future transport solutions

---

## 🧪 Connections (GPS Module)

- VCC → 3.3V or 5V on RPi  
- GND → GND on RPi  
- TX → GPIO15 (UART RX)  
- RX → GPIO14 (UART TX)

---

## 🔗 Project Highlight

Check out our project featured on LinkedIn:  
👉 [AI + IoT for Road Safety – LinkedIn Post](https://www.linkedin.com/posts/bishoy-wasfey-49162433_ai-iot-roadsafety-activity-7298999531361202176-woZP?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFXH9UMB3_MYrKM8vMf-2n4K655DhAI6H5E)


## 🛡️ License

All rights reserved.  
This software may not be copied, modified, or redistributed without explicit permission from the authors.
