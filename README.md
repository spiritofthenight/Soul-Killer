# Soul-Killer
#### Have you ever felt you need to talk to someone just like yourself ?
  <p><b>you dont need to wait anymore !<br> 
    because project Soul Killer is designed for your need .
  </b></p>

## Project Soul Killer will let you TALK directly to yourself !
<p>the idea is :<br>
you will answer 100 question inside SoulKiller.py with 100% honesty<br>
then the app and model can ~100% act just like you !<br>
then you can interact with the model with a minimal yet clean UI<br>
and the model can talk to you with sound in realtime<br>
and all of this will happen <b>100% fully offline</b> on your computer !
</p>

## how to use ?
- first install ollama client app version 0.11.3 on your windows PC
then:
```bash
git clone https://github.com/spiritofthenight/Soul-Killer/.git
cd Soul-Killer
python -m venv .venv
.venv\scripts\activate
pip install -r requirements.txt
```
- then start ollama client app on your PC and close it (it will be running in the background)
- answer to 100 questions in SoulKiller.py with 100% honesty and define the role for the model inside SoulKiller.py
```bash
python SoulKiller.py
```
- disconnect your internet then Open your web browser and visit 127.0.0.1:5000
- start cahtting with yourself and redefine "Talking to myself"

### Required System:
- a Power full GPU with more than 8GB vram
- 12 GB+ RAM
- Windows 11
- python 3.12

#### if you get any error:
- check if ollama.exe is running in the background before running SoulKiller.py
- check all the dependencies are installed from requirements.txt
- make sure you have the required system to run a local model
- make sure no other app is using port 5000
- if you get a http error 500 or 503 , make sure no vpn is running and restart your PC once

*this project was inspired by the project soul killer in cyberpunk 2077 video game*
