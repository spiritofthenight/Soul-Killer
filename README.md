# Soul-Killer
#### Have you ever felt you need to talk to someone just like yourself?
  <p><b>You don’t need to wait anymore!<br> 
    Because project Soul Killer is designed for your need.
  </b></p>

## Project Soul Killer will let you TALK directly to yourself!
<p>The idea is:<br>
You will answer 100 questions inside SoulKiller.py with 100% honesty<br>
Then the app and model can ~100% act just like you!<br>
Then you can interact with the model with a minimal yet clean UI<br>
And the model can talk to you with sound in real time<br>
And all of this will happen <b>100% fully offline</b> on your computer!
</p>

## How to use?
- First install Ollama client app version 0.11.3 on your Windows PC  
Then:
git clone https://github.com/spiritofthenight/Soul-Killer/.git
cd Soul-Killer
python -m venv .venv
.venv\scripts\activate
pip install -r requirements.txt

- Then start Ollama client app on your PC and close it (it will be running in the background)
- Answer the 100 questions in SoulKiller.py with 100% honesty and define the role for the model inside SoulKiller.py
python SoulKiller.py

- Disconnect your internet, then open your web browser and visit 127.0.0.1:5000
- Start chatting with yourself and redefine "Talking to myself"

### Required System:
- A powerful GPU with more than 8GB VRAM
- 12 GB+ RAM
- Windows 11
- Python 3.12

#### If you get any error:
- Check if ollama.exe is running in the background before running SoulKiller.py
- Check all the dependencies are installed from requirements.txt
- Make sure you have the required system to run a local model
- Make sure no other app is using port 5000
- If you get an HTTP error 500 or 503, make sure no VPN is running and restart your PC once

*This project was inspired by the project Soul Killer in the Cyberpunk 2077 video game*
