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
    path('', include(router.urls)),
]
