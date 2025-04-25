import requests, os
from dotenv import load_dotenv
load_dotenv()

def post_to_farcaster(content):
    payload = {"text": content, "signer_uuid": os.getenv("SIGNER_UUID")}
    headers = {"Content-Type": "application/json", "Accept": "application/json", "api_key": os.getenv("NEYNAR_API_KEY")}
    r = requests.post("https://api.neynar.com/v2/farcaster/cast", json=payload, headers=headers)
    print("[Farcaster]", r.status_code, r.text)
