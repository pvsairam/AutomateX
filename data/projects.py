import random

def get_random_project():
    with open("data/projects.txt") as f:
        return random.choice([line.strip() for line in f if line.strip()])
