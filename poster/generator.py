import os
from dotenv import load_dotenv
import openai, requests
import google.generativeai as genai

load_dotenv()

def generate_post(project):
    try:
        openai.api_key = os.getenv("CHATGPT_API_KEY")
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Write a short bullish post about {project} under 280 chars."}]
        )
        return res.choices[0].message.content.strip()
    except:
        try:
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(f"Write a bullish post under 280 chars about {project}.")
            return response.text.strip()
        except:
            try:
                headers = {
                    "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": "deepseek-chat",
                    "messages": [{"role": "user", "content": f"Write a bullish post about {project}."}]
                }
                r = requests.post("https://api.deepseek.com/v1/chat/completions", headers=headers, json=payload)
                return r.json()["choices"][0]["message"]["content"].strip()
            except:
                return f"{project} is heating up! Big alpha incoming. 🚀"
