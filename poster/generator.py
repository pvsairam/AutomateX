import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def generate_post(project):
    # Try ChatGPT
    try:
        print("[GENERATOR] Trying ChatGPT...")
        client = OpenAI(api_key=os.getenv("CHATGPT_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user",
                "content": f"Write a short, bullish Web3 tweet (under 280 chars) about {project}, no hashtags, no spam."
            }]
        )
        text = response.choices[0].message.content.strip()
        print("[GENERATOR] ChatGPT success.")
        return text
    except Exception as e:
        print("[GENERATOR] ChatGPT failed:", str(e))

    # Try Gemini
    try:
        print("[GENERATOR] Trying Gemini...")
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel("models/gemini-pro")
        response = model.generate_content(
            f"Write a short, bullish Web3 tweet under 280 characters about {project}, no hashtags, no spam."
        )
        print("[GENERATOR] Gemini success.")
        return response.text.strip()
    except Exception as e:
        print("[GENERATOR] Gemini failed:", str(e))

    # DeepSeek skipped
    print("[GENERATOR] DeepSeek skipped (payment required).")

    # All LLMs failed — do not post anything
    print("[GENERATOR] All LLMs failed. Skipping this project.")
    return None
