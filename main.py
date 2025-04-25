import schedule, time
from poster.generator import generate_post
from poster.memory import already_posted, save_post
from poster.farcaster import post_to_farcaster
from poster.telegram import log_to_telegram
from data.projects import get_random_project

def job():
    project = get_random_project()
    text = generate_post(project)
    if already_posted(text): return
    post_to_farcaster(text)
    log_to_telegram(text)
    save_post(text)

schedule.every(1).hours.do(job)
job()
while True:
    schedule.run_pending()
    time.sleep(60)
