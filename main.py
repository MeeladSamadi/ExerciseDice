# main.py
from dice import roll_dice
from exercise import get_exercise
from tracker import Tracker

def main():
    tracker = Tracker()
    while True:
        input("Press Enter to roll the dice for your fitness challenge...")
        roll = roll_dice()
        exercise = get_exercise(roll)
        print(f"You rolled a {roll}. Your challenge: {exercise}")
        tracker.complete_challenge()
        tracker.log_results(exercise)
        print(f"Total challenges completed: {tracker.get_completed_challenges()}")
        cont = input("Do you want to roll again? (y/n): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()