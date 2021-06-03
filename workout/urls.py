from django.urls import path
from django.urls import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'MuscleGroup', views.MuscleGroupView)
router.register(r'ExerciseEquipment', views.ExerciseEquipmentView)
router.register(r'ExerciseStep', views.ExerciseStepView)
router.register(r'Exercise', views.ExerciseView)
router.register(r'ExerciseInWorkout', views.ExerciseInWorkoutView)
router.register(r'WorkoutSession', views.WorkoutSessionView)
router.register(r'WorkoutPlan', views.WorkoutPlanView)



app_name = 'fitdiet'
urlpatterns = [
    path('', include(router.urls)),
]
