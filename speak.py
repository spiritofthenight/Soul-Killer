# https://github.com/spiritofthenight/
import sys
import json
import pyttsx3

def list_voices():
    engine = pyttsx3.init()
    default_voice_id = engine.getProperty("voice")
    result = []
    for v in engine.getProperty("voices"):
        # Normalize language display
        langs = getattr(v, "languages", ["Unknown"])
        lang = langs[0].decode("utf-8") if hasattr(langs[0], "decode") else str(langs[0])
        result.append({
            "id": v.id,
            "name": getattr(v, "name", "Unknown"),
            "gender": getattr(v, "gender", "Unknown"),
            "language": lang
        })
    print(json.dumps({"voices": result, "default_voice_id": default_voice_id}))
    sys.exit(0)

def speak_once(text, voice_id=None):
    engine = pyttsx3.init()
    if voice_id:
        engine.setProperty("voice", voice_id)
    engine.say(text)
    engine.runAndWait()
    # engine stops when process exits

if __name__ == "__main__":
    if "--list-voices" in sys.argv:
        list_voices()
    elif "--speak" in sys.argv:
        data = sys.stdin.read()
        try:
            payload = json.loads(data) if data else {}
            text = payload.get("text", "")
            voice_id = payload.get("voice_id")
            if text:
                speak_once(text, voice_id)
        except Exception as e:
            print(f"Speak error: {e}", file=sys.stderr)
    else:
        print("Usage: speak.py --list-voices | --speak", file=sys.stderr)
        sys.exit(1)
