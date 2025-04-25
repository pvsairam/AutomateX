import os, requests
from dotenv import load_dotenv
load_dotenv()

def log_to_telegram(text):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    r = requests.post(f"https://api.telegram.org/bot{token}/sendMessage", data={"chat_id": chat_id, "text": text})
    print("[Telegram]", r.status_code, r.text)
