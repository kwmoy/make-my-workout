class Exercise:
    def __init__(self, tips: list[str], equipment: set,
                 muscles: set,
                 push_pull: str):
        self.tips = tips
        self.equipment = equipment
        self.muscles = muscles
        self.exercise_type = self.derive_isolation_or_compound()
        self.upper_or_lower = self.derive_upper_or_lower()
        self.push_pull = push_pull

    def derive_isolation_or_compound(self):
        return ExerciseType.compound if len(self.muscles)>1 else ExerciseType.isolation

    def derive_upper_or_lower(self):
        upper = any(muscle in UPPER_MUSCLES for muscle in self.muscles)
        lower = any(muscle in LOWER_MUSCLES for muscle in self.muscles)
        if upper and lower:
            return UpperOrLower.full_body
        elif upper:
            return UpperOrLower.upper
        else:
            return UpperOrLower.lower


class ExerciseType:
    isolation = "isolation"
    compound = "compound"


class Equipment:
    mini_looped_bands = "Mini Looped Bands"
    large_looped_bands = "Large Looped Bands"
    tubed_bands = "Tubed Resistance Bands"
    tubed_bands_and_stationary_object = "Tubed Resistance Bands and Stationary Object"
    dumbbell = "Dumbbell"
    none_needed = "None Needed"
    gym = "Gym"


EQUIPMENT_GROUPED = {
    "resistance bands": [
        Equipment.tubed_bands,
        Equipment.mini_looped_bands,
        Equipment.large_looped_bands,
        Equipment.tubed_bands_and_stationary_object,
    ],
    "weights": [
        Equipment.dumbbell
    ]
}

class Muscles:
    abs = "Abs"
    back = "Back"
    biceps = "Biceps"
    chest = "Chest"
    forearms = "Forearms"
    shoulders = "Shoulders"
    triceps = "Triceps"

    calves = "Calves"
    glutes = "Glutes"
    hamstrings = "Hamstrings"
    quads = "Quadriceps"

UPPER_MUSCLES = {Muscles.abs, Muscles.back, Muscles.biceps,
                 Muscles.chest, Muscles.forearms, Muscles.shoulders, Muscles.triceps}

LOWER_MUSCLES = {Muscles.calves, Muscles.glutes, Muscles.hamstrings, Muscles.quads}

class UpperOrLower:
    upper = "Upper"
    lower = "Lower"
    full_body = "Full"

class PushOrPull:
    push = "Push"
    pull = "Pull"
    both = "Both"