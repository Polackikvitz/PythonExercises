import random


class Weightlifter:
    def __init__(self, intensity_level, weight, age, name):
        self.weights = []
        self.rest_days = 0
        self.intensity_level = intensity_level
        self.weight = weight
        self.age = age
        self.name = name

    def exercise_days(self):
        if self.intensity_level < 0 or self.intensity_level > 100:
            raise ValueError('intensity level must be between 0 and 100')
        elif self.intensity_level > 0 and self.intensity_level <= 20:
            self.rest_days = 3
        elif self.intensity_level < 50 and self.intensity_level > 20:
            self.rest_days = 2
        elif self.intensity_level >= 50 and self.intensity_level <= 100:
            self.rest_days = 1

        number_of_exercises = 7 - self.rest_days
        return number_of_exercises

    def get_exercises(self, exercises):  #exercises = instance of class Exercises
        exercise_dict = {}
        muscle_group_keys = exercises.get_muscle_groups()
        number_of_exercises = self.exercise_days()

        # TODO: POP USED EXERCISES
        for day in range(number_of_exercises):
            muscle_group = random.choice(muscle_group_keys)
            exercise = []
            muscle_group_exercises = exercises.muscle_group_exercises.get(muscle_group, [])

            for muscle, exercise_options in muscle_group_exercises.items():
                muscle_group_exercise = muscle + ': ' + random.choice(exercise_options)
                exercise.append(muscle_group_exercise)

            exercise_dict[day] = exercise

        return exercise_dict

    def __repr__(self):
        exercises = Exercises()
        exercise_dict = self.get_exercises(exercises)
        exercise_list_str = '\n'.join([f'Day {day + 1}: ' + '; '.join(exs) for day, exs in exercise_dict.items()])
        display = (f'Name: {self.name}\nAge: {self.age}\nWeight: {self.weight}\n\n'
                   f'Ready to rumble {self.name}!! It looks like this week is going to be:\n\n{exercise_list_str}.')
        return display


class Exercises:
    def __init__(self):
        self.muscle_group_exercises = {
            'legs': {
                'Quadriceps': ['Squats', 'Lunges', 'Leg presses'],
                'Hamstrings': ['Deadlifts', 'Leg curls'],
                'Adductors': ['Inner thigh exercises', 'Adductor machine'],
                'Glutes': ['Glute bridges', 'Hip thrusts'],
                'Calves': ['Calf raises'],
                'Tibialis Anterior': ['Toe raises'],
                'Hip Flexors': ['Leg raises', 'Hip flexor stretches']
            },
            'chest': {
                'Pectoralis Major': ['Bench Press', 'Push-Ups', 'Chest Flyes', 'Cable Crossover'],
                'Pectoralis Minor': ['Chest Dips', 'Pushup w/ Narrow Grip', 'Incline Dumbbell Flyes']
            },
            'deltoids': {
                'Anterior Deltoid': ['Front Raises', 'Overhead Press', 'Arnold Press', 'Dumbbell Shoulder Press'],
                'Lateral Deltoid': ['Lateral Raises', 'Upright Rows', 'Cable Lateral Raises'],
                'Posterior Deltoid': ['Rear Delt Flyes', 'Face Pulls', 'Reverse Pec Deck', 'Bent-Over Lateral Raises']
            },
            'back': {
                "Trapezius": ["Barbell shrugs", "Dumbbell shrugs", "Face pulls"],
                "Latissimus dorsi (Lats)": ["Pull-ups", "Lat pulldowns", "Rows"],
                "Rhomboids": ["Bent-over rows", "Cable rows", "Reverse flyes"],
                "Erector spinae (Lower back)": ["Deadlifts", "Back extensions", "Good mornings"],
                "Teres major and minor": ["Inverted rows", "Straight-arm pulldowns"]
            },
            'biceps': {
                "Biceps brachii": ["Barbell curls", "Dumbbell curls", "Hammer curls"],
                "Brachialis": ["Reverse curls", "Cable curls"],
                "Brachioradialis": ["Wrist curls", "Zottman curls"]
            },
            'triceps': {
                "Triceps brachii (Lateral head)": ["Tricep pushdowns", "Overhead tricep extensions", "Skull crushers"],
                "Triceps brachii (Long head)": ["Close-grip bench press", "Dips", "French press"],
                "Triceps brachii (Medial head)": ["Diamond push-ups", "Tricep kickbacks"]
            },
            'ab_muscles': {
                "Rectus abdominis (Six-pack muscles)": ["Crunches", "Leg raises", "Hanging knee raises"],
                "Obliques (Internal and External)": ["Russian twists", "Side plank", "Bicycle crunches"],
                "Transversus abdominis": ["Planks", "Vacuum exercises", "Dead bug"]
            }
        }

    def get_muscle_groups(self):
        return list(self.muscle_group_exercises.keys())


exercises = Exercises()
weightlifter1 = Weightlifter(intensity_level=100, weight=180, age=30, name='Calvin Berndt')
weightlifter_exercises = weightlifter1.get_exercises(exercises)
print(weightlifter1)
