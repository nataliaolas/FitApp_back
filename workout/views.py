from .serializers import ExerciseEquipmentSerializer, ExerciseInWorkoutSerializer, ExerciseSerializer, ExerciseStepSerializer, FavouriteExerciseSerializer, FavouriteWorkoutPlanSerializer, FavouriteWorkoutSessionSerializer, MuscleGroupSerializer, WorkoutPlanSerializer, WorkoutSessionSerializer
from .models import Exercise, ExerciseEquipment, ExerciseInWorkout, ExerciseStep, FavouriteExercise, FavouriteWorkoutPlan, FavouriteWorkoutSession, MuscleGroup, WorkoutPlan, WorkoutSession
from rest_framework import mixins
from rest_framework import viewsets
# Create your views here.


class MuscleGroupView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer

class ExerciseEquipmentView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = ExerciseEquipment.objects.all()
    serializer_class = ExerciseEquipmentSerializer

class ExerciseStepView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = ExerciseStep.objects.all()
    serializer_class = ExerciseStepSerializer


class ExerciseView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class ExerciseInWorkoutView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = ExerciseInWorkout.objects.all()
    serializer_class = ExerciseInWorkoutSerializer

class WorkoutSessionView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer

class WorkoutPlanView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer

class FavouriteExerciseView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = FavouriteExercise.objects.all()
    serializer_class = FavouriteExerciseSerializer

class FavouriteWorkoutSessionView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = FavouriteWorkoutSession.objects.all()
    serializer_class = FavouriteWorkoutSessionSerializer

class FavouriteWorkoutPlanView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = FavouriteWorkoutPlan.objects.all()
    serializer_class = FavouriteWorkoutPlanSerializer