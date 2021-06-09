import datetime
from typing import List
from .serializers import ExerciseEquipmentSerializer, ExerciseInWorkoutSerializer, ExerciseInWorkoutWithExerciseNameSerializer, ExerciseSerializer, ExerciseStepSerializer, FavouriteExerciseSerializer, FavouriteWorkoutPlanSerializer, FavouriteWorkoutSessionSerializer, MuscleGroupSerializer, USerWorkoutPlanSerializer, UserWorkoutSessionSerializer, WorkoutPlanSerializer, WorkoutSessionSerializer
from .models import Exercise, ExerciseEquipment, ExerciseInWorkout, ExerciseStep, FavouriteExercise, FavouriteWorkoutPlan, FavouriteWorkoutSession, MuscleGroup, UserWorkoutPlan, UserWorkoutSession, WorkoutPlan, WorkoutSession
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from braces.views import CsrfExemptMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
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
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]

    def create(self, request, *args, **kwargs):
        print("\n\n ***************\n")
        print(request.data)
        print("\n\n **************** \n")
        print("\n\n ***************\n")
        print(request.data['muscle_groups'])
        muscle_groups_list = []
        muscle_groups_list.append(request.data['muscle_groups'])
        request.data['muscle_groups'] = muscle_groups_list
        print(request.data['muscle_groups'])
        print("\n\n **************** \n")
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        print("\n\n ***************\n")
        print(request.data)
        print("\n\n **************** \n")
        print("\n\n ***************\n")
        print(request.data['muscle_groups'])
        is_muscle_groups_list = isinstance(request.data['muscle_groups'], list)
        if is_muscle_groups_list == False:
            muscle_groups_list = []
            muscle_groups_list.append(request.data['muscle_groups'])
            request.data['muscle_groups'] = muscle_groups_list
        print(request.data['muscle_groups'])
        print("\n\n **************** \n")
        return super().update(request, *args, **kwargs)



@api_view(['GET'])
def user_fav_exercise_view(request,pk):
    if request.method == 'GET':
        user_favourites = FavouriteExercise.objects.filter(user=pk)
        fav_exercises_id_list = []
        for i in user_favourites:
            fav_exercises_id_list.append(i.exercise.id)
        filtered_list = Exercise.objects.filter(id__in=fav_exercises_id_list)
        serializer = ExerciseSerializer(filtered_list,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def user_fav_workoutplan_view(request,pk):
    if request.method == 'GET':
        user_favourites = FavouriteWorkoutPlan.objects.filter(user=pk)
        fav_exercises_id_list = []
        for i in user_favourites:
            fav_exercises_id_list.append(i.workout_plan.id)
        filtered_list = WorkoutPlan.objects.filter(id__in=fav_exercises_id_list)
        serializer = WorkoutPlanSerializer(filtered_list,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def user_fav_workoutsession_view(request,pk):
    if request.method == 'GET':
        user_favourites = FavouriteWorkoutSession.objects.filter(user=pk)
        fav_exercises_id_list = []
        for i in user_favourites:
            fav_exercises_id_list.append(i.workout_session.id)
        filtered_list = WorkoutSession.objects.filter(id__in=fav_exercises_id_list)
        serializer = WorkoutSessionSerializer(filtered_list,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def user_exercises(request,pk):
    if request.method == 'GET':
        exercise = Exercise.objects.filter(author=pk)
        serializer = ExerciseSerializer(exercise,many=True)
        return Response(serializer.data)
    return Response("Cos nie pyklo")

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

    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]


class WorkoutPlanView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]



class UserWorkoutPlanView(CsrfExemptMixin,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = UserWorkoutPlan.objects.all()
    serializer_class = USerWorkoutPlanSerializer


@api_view(['GET'])
def workout_sessions_in_plan(request,pk):
    if request.method == 'GET':
        workout_plan = WorkoutPlan.objects.get(id=pk)
        workout_sessions = workout_plan.workout_sessions
        serializer = WorkoutSessionSerializer(workout_sessions,many=True)
        return Response(serializer.data)
    return Response("Cos nie pyklo")

# @api_view(['GET'])
# def exercise_in_workout_with_exercise_names(request, pk):
#     if request.method == 'GET':
#         exercise_in_workout = ExerciseInWorkout.objects.filter(workout_session=pk)
#         serializer = ExerciseInWorkoutWithExerciseNameSerializer(exercise_in_workout,many=True)
#         return Response(serializer.data)
#     return Response("Cos nie pyklo")

@api_view(['GET'])
def current_workout_session(request,pk):
    if request.method == 'GET':
        workout_plan = UserWorkoutPlan.objects.get(id=pk)
        now = datetime.datetime.now()
        workout_session = UserWorkoutSession.objects.get(workout_plan=workout_plan, date_of_workout=now)
        if workout_session:
            serializer = UserWorkoutSessionSerializer(workout_session)
        else:
            return Response("Nie ma dzisiaj treningu.")
        return Response(serializer.data)
    return Response("Cos nie pyklo")


class FavouriteExerciseView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = FavouriteExercise.objects.all()
    serializer_class = FavouriteExerciseSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['user',]


class FavouriteWorkoutSessionView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = FavouriteWorkoutSession.objects.all()
    serializer_class = FavouriteWorkoutSessionSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['user',]


class FavouriteWorkoutPlanView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = FavouriteWorkoutPlan.objects.all()
    serializer_class = FavouriteWorkoutPlanSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['user',]

    
class ExerciseInWorkoutSessionWithExerciseName(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = ExerciseInWorkout.objects.all()
    serializer_class = ExerciseInWorkoutWithExerciseNameSerializer
    filter_backends = [DjangoFilterBackend]
    search_fields = ['workout_session',]