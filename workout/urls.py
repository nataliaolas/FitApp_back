from django.urls import path
from django.urls import include
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
router = routers.SimpleRouter()
router.register(r'MuscleGroup', views.MuscleGroupView)
router.register(r'ExerciseEquipment', views.ExerciseEquipmentView)
router.register(r'ExerciseStep', views.ExerciseStepView)
router.register(r'Exercise', views.ExerciseView)
router.register(r'ExerciseInWorkout', views.ExerciseInWorkoutView)
router.register(r'WorkoutSession', views.WorkoutSessionView)
router.register(r'WorkoutPlan', views.WorkoutPlanView)
router.register(r'UserWorkoutPlan', views.UserWorkoutPlanView)
router.register(r'FavouriteExercise', views.FavouriteExerciseView)
router.register(r'FavouriteWorkoutSession', views.FavouriteWorkoutSessionView)
router.register(r'FavouriteWorkoutPlan', views.FavouriteWorkoutPlanView)


app_name = 'fitdiet'
urlpatterns = [
     path('workoutplansessions/<int:pk>', views.workout_sessions_in_plan),
     path('userexercises/<int:pk>', views.user_exercises),
     # path('exercises_in_session/<int:pk>',views.exercise_in_workout_with_exercise_names)
]
