import os
import openai
import requests
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def generate_post(project):
    # Try ChatGPT
    try:
        openai.api_key = os.getenv("CHATGPT_API_KEY")
        print("[GENERATOR] Trying ChatGPT...")
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": f"Write a short, bullish Web3 tweet (under 280 chars) about {project}, no hashtags, no spam."
            }]
        )
        print("[GENERATOR] ChatGPT success.")
        return res.choices[0].message.content.strip()
    except Exception as e:
        print("[GENERATOR] ChatGPT failed:", str(e))

    # Try Gemini
    try:
        print("[GENERATOR] Trying Gemini...")
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(
            f"Write a short, bullish Web3 tweet under 280 characters about {project}, no hashtags, no spam."
        )
        print("[GENERATOR] Gemini success.")
        return response.text.strip()
    except Exception as e:
        print("[GENERATOR] Gemini failed:", str(e))

    # Try DeepSeek
    try:
        print("[GENERATOR] Trying DeepSeek...")
        headers = {
            "Authorization": f"Bearer {os.getenv('DEEPSEEK_API_KEY')}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "deepseek-chat",
            "messages": [{
                "role": "user",
                "content": f"Write a short, bullish Web3 tweet under 280 characters about {project}, no hashtags, no spam."
            }]
        }
        r = requests.post("https://api.deepseek.com/v1/chat/completions", headers=headers, json=payload)
        r.raise_for_status()
        print("[GENERATOR] DeepSeek success.")
        return r.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("[GENERATOR] DeepSeek failed:", str(e))

    # No fallback
    print("[GENERATOR] All LLMs failed. No post will be generated.")
    return None
