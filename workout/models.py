from django.db import models
from django.contrib.auth.models import User
"""
TODO:
    Napisac testy dla modeli
"""


class MuscleGroup(models.Model):
    """ model for predefined/or added by admin/moderator muscles groups """
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ExerciseEquipment(models.Model):
    """ model for predefined/or added by admin/moderetor exercise equipments"""
    name = models.TextField()

    def __str__(self):
        return self.name


class Exercise(models.Model):
    """ model that contains information about exercise"""
    name = models.CharField(max_length=30)
    picture = models.ImageField(
        'Zdjecie cwiczenia',
        null=True,
        blank=True,
        upload_to='workout/exercise')
    public = models.BooleanField(default=True)
    description = models.TextField()
    muscle_groups = models.ManyToManyField(MuscleGroup)
    exercise_equipment = models.ForeignKey(
        ExerciseEquipment, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_exercise_steps(self):
        return self.steps.all()

class UserExercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.exercise.name + " " + self.user.username

class ExerciseStep(models.Model):
    """ model for steps one's need to do during exercise """
    step = models.CharField(max_length=100)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True, related_name='steps')


class WorkoutPlan(models.Model):
    name = models.CharField(max_length=30)
    picture = models.ImageField(
        'Zdjecie planu treningowego', null=True, blank=True, upload_to='workout/plans')
    description = models.TextField()
    duration_in_days = models.IntegerField(default=5)
    workout_sessions = models.ManyToManyField('WorkoutSession')

    def __str__(self):
        return self.name + " czas trwania " + str(self.duration_in_days) +" dni"


class WorkoutSession(models.Model):
    """ model that represents workout session """
    name = models.CharField(max_length=30)
    picture = models.ImageField(
        'Zdjecie sesji treningowej',
        null=True,
        blank=True,
        upload_to='workout/sessions')
    time_of_workout = models.CharField(max_length=15, default="45 minut")
    trained_muscles = models.ManyToManyField(MuscleGroup)

    def __str__(self):
        return self.name

    def get_exercises(self):
        return self.exerciseinworkout_set.all()


class UserWorkoutSession(models.Model):
    workout_plan = models.ForeignKey(
        'UserWorkoutPlan', on_delete=models.CASCADE)
    date_of_workout = models.DateField()
    workout_session = models.ForeignKey(
        WorkoutSession, on_delete=models.CASCADE)


class UserWorkoutPlan(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_plan = models.ForeignKey(
        WorkoutPlan, on_delete=models.CASCADE)

    


class ExerciseInWorkout(models.Model):
    """ model that represents the whole exercise(number of reps, sets and rest time) in workout """
    exercise = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, null=True)
    workout_session = models.ForeignKey(
        WorkoutSession, on_delete=models.CASCADE)
    load_range = models.CharField(
        max_length=30, blank=True, default="Brak ciężaru - 10% ONE-RM")
    min_repetitions = models.IntegerField(default=4)
    max_repetitions = models.IntegerField(default=8)
    number_of_sets = models.IntegerField(default=4)
    rest_between_sets = models.CharField(max_length=40, default="1 minuta")
    rest_after_exercise = models.CharField(max_length=20, default="2 minuty")

    def __str__(self):
        return self.workout_session.name + " " + self.exercise.name + " sets: " + str(self.number_of_sets)


class FavouriteExercise(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.exercise.name + " " + self.user.username


class FavouriteWorkoutSession(models.Model):
    workout_session = models.ForeignKey(
        WorkoutSession, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True)


class FavouriteWorkoutPlan(models.Model):
    workout_plan = models.ForeignKey(
        WorkoutPlan, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
