LOG_FILE = "data/posted_log.txt"

def already_posted(text):
    try:
        with open(LOG_FILE, "r") as f:
            return text.strip() in f.read()
    except FileNotFoundError:
        return False

def save_post(text):
    with open(LOG_FILE, "a") as f:
        f.write(text.strip() + "\n")
