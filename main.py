import schedule, time
from config import USE_TWITTER, USE_FARCASTER
from poster.generator import generate_post
from poster.memory import already_posted, save_post
from poster.telegram import log_to_telegram
from poster.farcaster import post_to_farcaster
from poster.twitter import post_to_twitter
from data.projects import get_random_project

def job():
    project = get_random_project()
    text = generate_post(project)
    if already_posted(text): return
    if USE_FARCASTER:
        post_to_farcaster(text)
    if USE_TWITTER:
        post_to_twitter(text)
    log_to_telegram(text)
    save_post(text)

schedule.every(1).hours.do(job)
job()
while True:
    schedule.run_pending()
    time.sleep(60)
