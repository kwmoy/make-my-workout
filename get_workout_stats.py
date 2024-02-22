from exercise_objects import Exercise
from exercises import EXERCISES

workout_log = {
    "2024-01-06": ["Bicep Curl to Shoulder Press",
                   "Pushup",
                   "Glute Bridge",
                   "Squat", ],
    "2024-01-08": ["Bicep Curl to Shoulder Press",
                    "Lunge",
                    "Standing Glute Kickback",
                    "Sitting Leg Extension",
                    "Squat and Overhead Press",
                    "Squat",
                    "Lat Pull-down",
                    "Pushup",
                   ],
    "2024-01-10": ["Bicep Curl to Shoulder Press",
                   ],
    "2024-01-11": ["Glute Bridge",
                    "Bicep Curl to Shoulder Press",
                    "Squat and Overhead Press",
                    "Lat Pull-down",
                   ],
    "2024-01-12": [  # Me: Pullups
                    "Pull-up",
                    # Me: Lateral raises, Lunges, Chest Press,
                    "Lateral Raise", "Lunge", "Bench Press",
                    # Class: Pushups, skull crushers, bench press
                    "Bench Press", "Tricep Extension", "Pushup",
                    # Class: Jumping jacks, high knees, situps
                    "Sit Up",
                    # Class: deadlifts, kettlebell swings, clean and press

                    # Class: Flat/90degree situps, rows, reverse flys
                    # Class: bicep curls
                    "Bicep Curl",

                   ],
    "2024-01-19": ["Single-Arm Row"],
    "2024-01-25": [
                    "Sit Up",
                    "Lat Pull-down",
                    "Plank",
                    "Lat Pull-down",
                    "Standing Glute Kickback",
                    "Pushup",
    ],
    "2024-02-03": [
        "Plank",
        "Bicep Curl to Shoulder Press",
        "Single-Arm Row",
        "Bicep Curl",
        "Lunge",
        "Lat Pull-down",
        "Sit Up",
        "Lateral Raise",
    ],
}


def get_muscles_worked(exercise_name:str) -> list[str]:
    return list(EXERCISES[exercise_name].muscles)


def get_all_muscles_worked_on_date(date:str) -> list[str]:
    # Choice 1: Get muscles worked on specific date
    return sum([get_muscles_worked(exercise) for exercise in workout_log[date]],[])

    # Choice 2: Calculate muscles worked in all exercises
    # return sum([get_muscles_worked(exercise) for exercise in EXERCISES],[])


# muscles_worked_list = sum([get_all_muscles_worked_on_date(str_date) for str_date in ["2024-01-10","2024-01-11"]], [])
muscles_worked_list = sum([get_all_muscles_worked_on_date(str_date) for str_date in workout_log.keys()], [])
muscles_dict = {muscle: muscles_worked_list.count(muscle) for muscle in set(muscles_worked_list)}
print(muscles_dict)
