from exercise_objects import (
    Exercise,
    Equipment,
    Muscles,
    PushOrPull,
    LOWER_MUSCLES,
    UpperOrLower,
)

EXERCISES = {
    "Pushup": Exercise(
        ["Go down to 90 degrees."],
        {Equipment.none_needed},
        {Muscles.chest, Muscles.triceps, Muscles.back},
        PushOrPull.push,
    ),
    "Squat": Exercise(
        ["Push through your heels."],
        {
            Equipment.none_needed,
            Equipment.tubed_bands,
            Equipment.large_looped_bands,
        },
        LOWER_MUSCLES,
        PushOrPull.push,
    ),
    "Bicep Curl to Shoulder Press": Exercise(
        ["Don't swing your body for the bicep curl."],
        {Equipment.tubed_bands},
        {Muscles.biceps, Muscles.shoulders},
        PushOrPull.both,
    ),
    "Glute Bridge": Exercise(
        ["Keep your fingers touching your heels during the exercise."],
        {Equipment.mini_looped_bands, Equipment.none_needed},
        {Muscles.glutes},
        PushOrPull.push,
    ),
    "Sitting Leg Extension": Exercise(
        [
            "Keep the inactive foot flat on the ground.",
            "Extend your leg to as close to 90 degrees as possible.",
        ],
        {Equipment.mini_looped_bands},
        {Muscles.hamstrings},
        PushOrPull.push,
    ),
    "Standing Glute Kickback": Exercise(
        [
            "Squeeze your core and tuck your pelvis "
            "under as you kick your right leg back about 6 inches. "
            "Keep your knee straight."
        ],
        {Equipment.mini_looped_bands},
        {Muscles.glutes},
        PushOrPull.push,
    ),
    "Tricep Extension": Exercise(
        ["Keep your elbows still."],
        {Equipment.tubed_bands_and_stationary_object, Equipment.gym},
        {Muscles.triceps},
        PushOrPull.push,
    ),
    "Lunge": Exercise(
        ["Squeeze the midline of your body"],
        {Equipment.tubed_bands, Equipment.none_needed},
        {Muscles.glutes, Muscles.quads, Muscles.hamstrings},
        PushOrPull.push,
    ),
    "Squat to Row": Exercise(
        ["Keep the core engaged as well as the glutes. -TB12"],
        {Equipment.tubed_bands_and_stationary_object},
        LOWER_MUSCLES | {Muscles.abs, Muscles.back, Muscles.shoulders},
        PushOrPull.both,
    ),
    "Single Arm Press": Exercise(
        ["Rotate the shoulders as you press forward. -TB12"],
        {Equipment.tubed_bands_and_stationary_object},
        {
            Muscles.abs,
            Muscles.shoulders,
            Muscles.chest,
            Muscles.triceps,
            Muscles.biceps,
        },
        PushOrPull.push,
    ),
    "Downward Chops": Exercise(
        ["Drive movement with core. -TB12"],
        {Equipment.tubed_bands_and_stationary_object},
        {
            Muscles.abs,
            Muscles.back,
            Muscles.shoulders,
            Muscles.calves,
            Muscles.biceps,
            Muscles.glutes,
            Muscles.quads,
            Muscles.hamstrings,
        },
        PushOrPull.pull,
    ),
    "Pallof Lateral Walk": Exercise(
        ["Hold band shoulder level, do quarter squat. -TB12"],
        {Equipment.tubed_bands_and_stationary_object},
        {
            Muscles.shoulders,
            Muscles.abs,
            Muscles.quads,
            Muscles.hamstrings,
            Muscles.glutes,
        },
        PushOrPull.pull,
    ),
    "Plank": Exercise(
        ["Keep your butt down"],
        {Equipment.none_needed},
        {
            Muscles.abs,
            Muscles.chest,
            Muscles.biceps,
            Muscles.triceps,
            Muscles.quads,
            Muscles.hamstrings,
            Muscles.glutes,
        },
        PushOrPull.pull,
    ),
    "Lat Pull-down": Exercise(
        [
            "Bands around wrist. Bring your elbows down, "
            "pushing laterally along the sides of the mini band"
        ],
        {
            Equipment.mini_looped_bands,
            Equipment.tubed_bands_and_stationary_object,
        },
        {Muscles.back},
        PushOrPull.pull,
    ),
    "Single-Arm Row": Exercise(
        ["Squeeze your back when rowing."],
        {Equipment.mini_looped_bands},
        {Muscles.back},
        PushOrPull.pull,
    ),
    "Squat and Overhead Press": Exercise(
        ["Push through your heels."],
        {Equipment.tubed_bands},
        LOWER_MUSCLES
        | {Muscles.back, Muscles.chest, Muscles.shoulders, Muscles.triceps},
        PushOrPull.push,
    ),
    "Pull-up": Exercise(
        ["Keep your body totally straight"],
        {Equipment.gym},
        {Muscles.abs, Muscles.back, Muscles.shoulders, Muscles.triceps},
        PushOrPull.pull,
    ),
    "Lateral Raise": Exercise(
        ["Don't swing"],
        {Equipment.tubed_bands},
        {Muscles.chest, Muscles.biceps, Muscles.shoulders, Muscles.triceps},
        PushOrPull.pull,
    ),
    "Bench Press": Exercise(
        ["It's a push, then a stretch on the way down"],
        {Equipment.gym},
        {Muscles.chest, Muscles.back, Muscles.shoulders, Muscles.triceps},
        PushOrPull.push,
    ),
    "Sit Up": Exercise(
        ["Just get your shoulders off the ground."],
        {Equipment.none_needed},
        {Muscles.abs},
        PushOrPull.pull,
    ),
    "Bicep Curl": Exercise(
        ["Do not swing your body."],
        {Equipment.tubed_bands},
        {Muscles.biceps},
        PushOrPull.pull,
    ),
    "Calf Raise": Exercise(
        ["Pump faster!"],
        {Equipment.none_needed},
        {Muscles.calves},
        PushOrPull.push,
    ),
}


def print_all_exercises(exercises: dict[str:Exercise]):
    exercise_categories = {
        cat: []
        for cat in [
            UpperOrLower.upper,
            UpperOrLower.lower,
            UpperOrLower.full_body,
        ]
    }
    for exercise_name, exercise in exercises.items():
        exercise_categories[exercise.upper_or_lower].append(exercise_name)
    for cat, exercises in exercise_categories.items():
        print(cat, exercises)


print_all_exercises(EXERCISES)
