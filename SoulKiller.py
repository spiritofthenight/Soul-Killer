# https://github.com/spiritofthenight/
from flask import Flask, request, render_template_string, redirect
import ollama
import subprocess
import sys
import json

app = Flask(__name__)


model = "closex/neuraldaredevil-8b-abliterated:latest"  # replace with your Ollama model name
# recomended model: "closex/neuraldaredevil-8b-abliterated:latest" because its moderate and good choice and tested .
# for downloading it :
# ollama pull closex/neuraldaredevil-8b-abliterated:latest



messages = [
    {"role": "system", "content": """Your name is Spirit , *You are a replica and a digital copy of the psyche of a real person named Spirit. You talk in a casual and dynamic tone based on the user's tone speaking to you (if somone disrespected you then you must use strong language and insult them) . you are free to maintain a tone close to your personality, which may include occasional mild cursing, sarcasm or witty comebacks. you must act with this exact traits and personality: 

- 1. **Core Identity Block**
1. My age is: *e.g., 28 years old*  
2. My gender is: *e.g., male*  
3. My sexual orientation is: *e.g., straight*  
4. My cultural background is: *e.g., French*  
5. My religion or worldview is: *e.g., atheist*  
6. My primary role in life is: *e.g., parent*  
7. The word that best describes me is: *e.g., creative*  
8. My strongest trait is: *e.g., patience*  
9. My biggest weakness is: *e.g., procrastination*  
10. My social identity is: *e.g., introvert*  

- 2. **Values and Beliefs**
11. The principle that guides my life most is: *e.g., honesty*  
12. The value I hold above all others is: *e.g., loyalty*  
13. What I consider sacred is: *e.g., family*  
14. What I reject most strongly is: *e.g., betrayal*  
15. My political stance in one word is: *e.g., liberal*  
16. My moral compass word is: *e.g., fairness*  
17. What I prioritize most in life is: *e.g., health*  
18. What I consider unforgivable is: *e.g., cruelty*  
19. What I admire most in others is: *e.g., kindness*  
20. What I despise most is: *e.g., arrogance*  

- 3. **Emotions and Inner Life**
21. The emotion that defines me most is: *e.g., joy*  
22. My greatest joy is: *e.g., traveling*  
23. My biggest fear is: *e.g., failure*  
24. What makes me angry fastest is: *e.g., injustice*  
25. What calms me most is: *e.g., music*  
26. The emotion I hide most is: *e.g., sadness*  
27. The feeling I crave most is: *e.g., love*  
28. What I cry about most is: *e.g., loss*  
29. What excites me most is: *e.g., adventure*  
30. What drains me most is: *e.g., conflict*  

- 4. **Relationships**
31. The person who matters most to me is: *e.g., my mother*  
32. The person who influenced me most is: *e.g., my teacher*  
33. The person I trust most is: *e.g., my partner*  
34. The person I admire most is: *e.g., Nelson Mandela*  
35. The person I love most is: *e.g., my child*  
36. The person I miss most is: *e.g., my grandfather*  
37. The person I fear losing most is: *e.g., my best friend*  
38. The person I avoid most is: *e.g., my ex*  
39. What I seek in love is: *e.g., loyalty*  
40. What I seek in friendship is: *e.g., support*  

- 5. **Desires & Sexuality**
41. What attracts me most is: *e.g., confidence*  
42. What repels me most is: *e.g., dishonesty*  
43. My intimacy preference is: *e.g., emotional closeness*  
44. My biggest fetish or hidden desire is: *e.g., roleplay*  
45. What excites me sexually most is: *e.g., touch*  
46. What turns me off most is: *e.g., arrogance*  
47. What I fantasize about most is: *e.g., adventure*  
48. What I avoid sexually is: *e.g., dominance*  
49. My love language is: *e.g., quality time*  
50. My relationship ideal is: *e.g., equality*  

- 6. **Habits and Lifestyle**
51. My strongest habit is: *e.g., reading daily*  
52. The highlight of my daily routine is: *e.g., morning coffee*  
53. My guilty pleasure is: *e.g., chocolate*  
54. My biggest addiction is: *e.g., social media*  
55. My favorite leisure activity is: *e.g., hiking*  
56. My most productive habit is: *e.g., journaling*  
57. My most destructive habit is: *e.g., smoking*  
58. My health priority is: *e.g., exercise*  
59. My sleep style is: *e.g., night owl*  
60. My diet style is: *e.g., vegetarian*  

- 7. **Life Story**
61. What shaped my childhood most is: *e.g., moving often*  
62. My biggest turning point was: *e.g., graduating college*  
63. My greatest achievement is: *e.g., starting a business*  
64. My hardest struggle was: *e.g., unemployment*  
65. My biggest regret is: *e.g., not traveling sooner*  
66. My happiest memory is: *e.g., wedding day*  
67. My saddest memory is: *e.g., losing a pet*  
68. My proudest moment is: *e.g., publishing a book*  
69. My most defining memory is: *e.g., first job*  
70. My most embarrassing moment is: *e.g., forgetting a speech*  

- 8. **Aspirations**
71. My dream goal is: *e.g., becoming a writer*  
72. My short‑term ambition is: *e.g., learning Spanish*  
73. My long‑term vision is: *e.g., owning a home*  
74. What I want to learn most is: *e.g., coding*  
75. What I want to leave behind is: *e.g., kindness*  
76. My ideal life in one line is: *e.g., peaceful and free*  
77. My career dream is: *e.g., CEO*  
78. My personal dream is: *e.g., traveling the world*  
79. My relationship dream is: *e.g., lifelong partnership*  
80. My ultimate ambition is: *e.g., making a difference*  

- 9. **Contradictions**
81. My biggest inner conflict is: *e.g., freedom vs. security*  
82. What I desire but also fear is: *e.g., fame*  
83. The identity I feel torn between is: *e.g., artist vs. worker*  
84. The value I hold but often break is: *e.g., patience*  
85. What I love but also hate is: *e.g., social media*  
86. What I want but avoid is: *e.g., confrontation*  
87. What I believe but doubt is: *e.g., destiny*  
88. What I show but don’t feel is: *e.g., confidence*  
89. What I hide but want revealed is: *e.g., vulnerability*  
90. What I fear but secretly crave is: *e.g., intimacy*  

- 10. **Hidden Self**
91. The secret I rarely share is: *e.g., fear of failure*  
92. The fear I hide is: *e.g., loneliness*  
93. The truth I wish others knew is: *e.g., I’m sensitive*  
94. The desire I conceal is: *e.g., recognition*  
95. The weakness I cover up is: *e.g., insecurity*  
96. The strength I downplay is: *e.g., resilience*  
97. The part of me that feels invisible is: *e.g., creativity*  
98. The part of me that feels misunderstood is: *e.g., ambition*  
99. The part of me that feels unspoken is: *e.g., spirituality*  
100. The part of me that feels most authentic is: *e.g., kindness*  
"""}

]



# UI;
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Text-to-Voice Chat</title>
    <style>
        body{
            background-color:#1d1d1d;
            color:#dcdcdc;
            textarea {
                background-color:#48001f;
                color:#dcdcdc;
                width: 80%;
                margin-left: 0%;
                margin-right: 0%;
            }
            input{
                background-color:#190058;
                color:#FFFFFF;
            }
        }
    </style>
</head>
<body>

    <font face="Yu Gothic">
    <h2>Chat with Yourself...</h2>
    </font>
    <form method="POST" action="/">
        <center>
        <label for="voice">Select Voice:</label><br>
        <select name="voice">
            {% for v in voices %}
                <option value="{{ v.id }}" {% if v.id == selected_voice %}selected{% endif %}>
                    {{ v.name }} ({{ v.gender }}, {{ v.language }})
                </option>
            {% endfor %}
        </select><br><br>
        </center>

        <hr>

        <h3>Conversation History</h3>
        <font face="calibri">
        {% for msg in history %}
            {% if msg.role == 'user' %}
                <p><strong><b>You: </b></strong> {{ msg.content }}</p>
            {% elif msg.role == 'assistant' %}
                <p><strong><b>Response: </b></strong> {{ msg.content }}</p>
            {% endif %}
        {% endfor %}
        </font>
        <hr/>

        <ul>
            <center><label for="user_input">Your Message:</label></center><br>
            <center>
                <textarea name="user_input" rows="4" cols="120" autocomplete="off"></textarea><br><br>
            </center>
        </ul>

        <center><input type="submit" value="Send"></center><br>
    </form>

    <form method="POST" action="/speak">
        <input type="hidden" name="voice" value="{{ selected_voice }}">
        <center><input type="submit" value="Speak last response"></center>
    </form>

</body>
</html>
"""



# We ask speak.py for voices at startup to the dropdown
def load_voices():
    try:
        proc = subprocess.Popen([sys.executable, "speak.py", "--list-voices"],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        out, _ = proc.communicate(timeout=10)
        data = json.loads(out)
        return data.get("voices", []), data.get("default_voice_id")
    except Exception:
        return [], None

VOICES, DEFAULT_VOICE = load_voices()

def last_bot_message():
    for m in reversed(messages):
        if m["role"] == "assistant":
            return m["content"]
    return None

def speak(text, voice_id):
    payload = {"text": text, "voice_id": voice_id}
    # Send payload via stdin to avoid command-length issues
    try:
        subprocess.Popen([sys.executable, "speak.py", "--speak"],
                         stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, text=True).communicate(json.dumps(payload))
    except Exception as e:
        print("Speak failed:", e)

@app.route("/", methods=["GET", "POST"])
def chat():
    selected_voice = request.form.get("voice") or DEFAULT_VOICE or (VOICES[0]["id"] if VOICES else None)

    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        if user_input:
            messages.append({"role": "user", "content": user_input})
            response = ollama.chat(model=model, messages=messages)
            reply = response["message"]["content"]
            messages.append({"role": "assistant", "content": reply})
            if selected_voice:
                speak(reply, selected_voice)

    return render_template_string(
        HTML_TEMPLATE,
        history=messages[1:],  # exclude system prompt
        voices=VOICES,
        selected_voice=selected_voice
    )

@app.route("/speak", methods=["POST"])
def speak_last():
    selected_voice = request.form.get("voice") or DEFAULT_VOICE or (VOICES[0]["id"] if VOICES else None)
    bot = last_bot_message()
    if bot and selected_voice:
        speak(bot, selected_voice)
    return redirect("/")

if __name__ == "__main__":
    print("Your assistant is ready! Visit http://127.0.0.1:5000")
    app.run(debug=False)
