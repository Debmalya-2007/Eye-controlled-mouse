 Eye Controlled Mouse

A Python app that lets you control your computer cursor using eye movements! It detects iris positions via your webcam using **MediaPipe FaceMesh** and moves the cursor smoothly. Blinking triggers clicks automatically.

---
Features
- Real-time iris tracking for hands-free cursor control  
- Adjustable smoothing for smooth pointer movement  
- Blink detection for click interaction  
- Visual feedback via webcam preview

---

## Tech Stack
- Python 3
- [OpenCV] – Video capture & processing  
- [MediaPipe] – Facial landmark/iris detection  
- [PyAutoGUI] – Cursor and click automation 

---

##  Setup
```bash
# 1️⃣ Clone the repo
git clone https://github.com/Debmalya-2007/Eye-controlled-mouse.git
cd Eye-controlled-mouse

# 2️⃣ Install dependencies
pip install -r Requirements.txt

# 3️⃣ Run the program
python eye_mouse.py
