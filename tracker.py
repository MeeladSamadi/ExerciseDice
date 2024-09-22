# tracker.py
from datetime import datetime

class Tracker:
    def __init__(self):
        self.completed_challenges = 0

    def complete_challenge(self):
        self.completed_challenges += 1

    def log_results(self, exercise):
        with open("log.txt", "a") as file:
            now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            file.write(f"{now} - Completed: {exercise}\n")

    def get_completed_challenges(self):
        return self.completed_challenges
