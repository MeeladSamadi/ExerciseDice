# exercise.py
exercises = {
    1: "10 Push-ups",
    2: "20 Sit-ups",
    3: "15 Squats",
    4: "30-second Plank",
    5: "10 Burpees",
    6: "20 Jumping Jacks"
}

def get_exercise(roll):
    return exercises.get(roll, "Rest Day")
