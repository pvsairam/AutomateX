import os
import tweepy
from dotenv import load_dotenv
load_dotenv()

def post_to_twitter(text):
    auth = tweepy.OAuth1UserHandler(
        os.getenv("TWITTER_API_KEY"),
        os.getenv("TWITTER_API_SECRET"),
        os.getenv("TWITTER_ACCESS_TOKEN"),
        os.getenv("TWITTER_ACCESS_SECRET")
    )
    api = tweepy.API(auth)
    try:
        api.update_status(status=text)
        print("[Twitter] Posted successfully.")
    except Exception as e:
        print("[Twitter Error]", str(e))
