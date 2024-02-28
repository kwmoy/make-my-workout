from exercise_objects import EQUIPMENT_GROUPED, Equipment
import math
from random import randrange

from exercises import EXERCISES


def _is_affirmative(text):
    return False if text.upper() != "Y" else True


def dismiss_athlete():
    print("Have a nice day!")
    quit()


def prompt_workout_desire():
    if not _is_affirmative(input("Want to work out today? (Y/N)")):
        dismiss_athlete()
    else:
        pass


def prompt_workout_duration():
    duration = input("How long (in minutes) can your workout be? ")
    if not (duration.isnumeric() and int(duration) > 0):
        print("Answer given is not a positive, whole number")
        dismiss_athlete()
    else:
        return int(duration)


def determine_number_exercises(duration):
    return math.floor(duration / 5)


def prompt_eligible_equipment():
    eligible_equipment = {Equipment.none_needed}
    for equipment_type, equipment in EQUIPMENT_GROUPED.items():
        if _is_affirmative(input(f"Do you have {equipment_type}? ")):
            for e in equipment:
                if _is_affirmative(input(f"Do you have {e} on hand? (Y/N) ")):
                    eligible_equipment.add(e)
    return eligible_equipment


def get_eligible_exercises(equipment_on_hand):
    return [
        e_name
        for e_name, e in EXERCISES.items()
        if any(eq in e.equipment for eq in equipment_on_hand)
    ]


def get_exercises(num_exercises, possible_exercises, upper_to_lower_ratio=0.5):
    # filter to eligible exercises
    if len(possible_exercises) > num_exercises:
        print("\nSelecting random exercises")
        selected_exercises = set()
        while len(selected_exercises) < num_exercises:
            rand_exercise = possible_exercises[
                randrange(len(possible_exercises))
            ]
            if rand_exercise not in selected_exercises:
                selected_exercises.add(rand_exercise)
        return selected_exercises
    else:
        print("You have too much time, you can complete all exercises")
        return possible_exercises


def get_random_exercises():
    prompt_workout_desire()
    max_duration = prompt_workout_duration()
    number_exercises = determine_number_exercises(max_duration)
    eligible_equipment = prompt_eligible_equipment()
    possible_exercises = get_eligible_exercises(eligible_equipment)
    exercises_for_workout = get_exercises(number_exercises, possible_exercises)

    print("Your exercises are:")
    for exercise in exercises_for_workout:
        print(exercise)
    return exercises_for_workout
