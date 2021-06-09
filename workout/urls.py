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
router.register(r'ExerciseInWorkoutSessionWithExerciseName', views.ExerciseInWorkoutSessionWithExerciseName)

app_name = 'fitdiet'
urlpatterns = [
     path('workoutplansessions/<int:pk>', views.workout_sessions_in_plan),
     path('userexercises/<int:pk>', views.user_exercises),
     path('current_workout_session/<int:pk>', views.current_workout_session),
     path('filtered_fav_ex/<int:pk>', views.user_fav_exercise_view),
     path('filtered_fav_wp/<int:pk>', views.user_fav_workoutplan_view),
     path('filtered_fav_ws/<int:pk>', views.user_fav_workoutsession_view)
     # path('exercises_in_session/<int:pk>',views.exercise_in_workout_with_exercise_names)
]
