# V2I-Cloud-connected-ADAS

An intelligent IoT-based driver assistance system using Raspberry Pi, GPS, and AI to enhance road safety by providing real-time traffic alerts and on-device traffic sign recognition.

---

## 📌 Features

- 📍 Real-time GPS tracking with Neo-6M module  
- ☁️ Cloud updates through ThingSpeak  
- 📱 Instant driver alerts via Blynk mobile app  
- 🧠 Offline AI-based traffic sign detection using YOLOv8  
- 🔋 Dual-mode operation (cloud + edge fallback)

---

## 🔧 System Components

| Component         | Description                                |
|------------------|--------------------------------------------|
| Raspberry Pi 3B+ | Core processing unit                        |
| Neo-6M GPS       | Provides live location data                |
| Pi Camera v1.3   | Captures road visuals for AI detection     |
| ThingSpeak       | Cloud platform for GPS data visualization  |
| Blynk            | Sends real-time alerts to the driver       |
| YOLOv8           | On-device traffic sign recognition         |

---

## 🔄 Workflow

1. 📡 GPS gathers real-time coordinates.
2. ☁️ Data is uploaded to ThingSpeak for monitoring.
3. 📲 Driver receives alerts via the Blynk app.
4. 📷 Camera captures signs; YOLOv8 handles detection locally if offline.

---

## 💡 Benefits

- ✅ Improved road safety and hazard awareness  
- ✅ Works with or without internet access  
- ✅ Detects traffic signs and issues alerts automatically  
- ✅ Portable and cost-efficient solution

---

## 🛠️ Technologies Used

- Python, OpenCV, PyTorch  
- Ultralytics YOLOv8  
- Blynk IoT Platform  
- ThingSpeak Cloud  
- Raspberry Pi OS

---

## 🛡️ License

All rights reserved.  
This software may not be copied, modified, or distributed without written permission from the author.

