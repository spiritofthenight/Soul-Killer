# Soul-Killer

> Have you ever felt you need to talk to someone just like yourself?

**You don't need to wait anymore!** Because project Soul Killer is designed for your need.

---

## 🎯 Project Overview

**Soul Killer will let you TALK directly to yourself!**

The idea:
- You will answer 100 questions inside SoulKiller.py with 100% honesty
- Then the app and model can ~100% act just like you!
- Then you can interact with the model with a minimal yet clean UI
- And the model can talk to you with sound in real time
- And all of this will happen **100% fully offline** on your computer!

*The logic was to keep everything simple and 100% offline*

---

## 🚀 How to use?

### Installation

First install Ollama client app version 0.11.3 on your Windows PC

```bash
git clone https://github.com/spiritofthenight/Soul-Killer/.git
cd Soul-Killer
ollama pull closex/neuraldaredevil-8b-abliterated:latest # or any other model you want
python -m venv .venv
.venv\scripts\activate
pip install -r requirements.txt
```

### Setup & Run

- Start Ollama client app on your PC and close it (it will be running in the background)
- Answer the 100 questions in SoulKiller.py with 100% honesty and define the role for the model inside SoulKiller.py

```bash
python SoulKiller.py
```

- Disconnect your internet, then open your web browser and visit `127.0.0.1:5000`
- Start chatting with yourself and redefine "Talking to myself"

---

## 💻 Required System

- A powerful GPU with more than 8GB VRAM
- 12 GB+ RAM
- Windows 11 (Tested only on Windows)
- Python 3.12

---

## ⚠️ Troubleshooting

If you get any error:
- Check if `ollama.exe` is running in the background before running SoulKiller.py
- Check all the dependencies are installed from requirements.txt
- Make sure you have the required system to run a local model
- Make sure no other app is using port 5000
- If you get an HTTP error 500 or 503, make sure no VPN is running and restart your PC once

---

*This project was inspired by the project Soul Killer in the Cyberpunk 2077 video game*
