from .serializers import ExerciseEquipmentSerializer, ExerciseInWorkoutSerializer, ExerciseSerializer, ExerciseStepSerializer, FavouriteExerciseSerializer, FavouriteWorkoutPlanSerializer, FavouriteWorkoutSessionSerializer, MuscleGroupSerializer, USerWorkoutPlanSerializer, WorkoutPlanSerializer, WorkoutSessionSerializer
from .models import Exercise, ExerciseEquipment, ExerciseInWorkout, ExerciseStep, FavouriteExercise, FavouriteWorkoutPlan, FavouriteWorkoutSession, MuscleGroup, UserWorkoutPlan, WorkoutPlan, WorkoutSession
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from braces.views import CsrfExemptMixin
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


class FavouriteExerciseView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = FavouriteExercise.objects.all()
    serializer_class = FavouriteExerciseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]

    def get_queryset(self):
    #TODO: Mozliwe ze trzeba to zrobic zeby zwracalo posilki(bo teraz to moze byc klopotliwe po froncie)
        return FavouriteExercise.objects.filter(user=self.request.user)

class FavouriteWorkoutSessionView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = FavouriteWorkoutSession.objects.all()
    serializer_class = FavouriteWorkoutSessionSerializer

    def get_queryset(self):
    #TODO: Mozliwe ze trzeba to zrobic zeby zwracalo posilki(bo teraz to moze byc klopotliwe po froncie)
        return FavouriteWorkoutSession.objects.filter(user=self.request.user)

class FavouriteWorkoutPlanView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = FavouriteWorkoutPlan.objects.all()
    serializer_class = FavouriteWorkoutPlanSerializer

    def get_queryset(self):
    #TODO: Mozliwe ze trzeba to zrobic zeby zwracalo posilki(bo teraz to moze byc klopotliwe po froncie)
        return FavouriteWorkoutPlan.objects.filter(user=self.request.user)