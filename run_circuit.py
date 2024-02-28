from exercise_objects import Exercise
from get_exercises import get_random_exercises
from sound_and_wait_helpers import (
    rest_and_introduce_exercise,
    run_active_exercise,
    rest_and_say_words,
)


def run_circuit(exercises: list[Exercise], active_time, rest_time):
    for exercise in exercises:
        rest_and_introduce_exercise(rest_time, exercise)
        run_active_exercise(active_time)


def rest_between_sets():
    pass


active_time = 40
rest_time = 20

my_exercises = get_random_exercises()
run_circuit(my_exercises, active_time, rest_time)
rest_and_say_words(
    active_time, "Round 1 is complete! One minute until round 2"
)
run_circuit(my_exercises, active_time, rest_time)
rest_and_say_words(
    active_time, "Round 2 is complete! One minute until round 3"
)
run_circuit(my_exercises, active_time, rest_time)
rest_and_say_words(active_time, "you're done!")
