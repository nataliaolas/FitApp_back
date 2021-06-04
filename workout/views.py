from .serializers import ExerciseEquipmentSerializer, ExerciseInWorkoutSerializer, ExerciseSerializer, ExerciseStepSerializer, FavouriteExerciseSerializer, FavouriteWorkoutPlanSerializer, FavouriteWorkoutSessionSerializer, MuscleGroupSerializer, USerWorkoutPlanSerializer, WorkoutPlanSerializer, WorkoutSessionSerializer
from .models import Exercise, ExerciseEquipment, ExerciseInWorkout, ExerciseStep, FavouriteExercise, FavouriteWorkoutPlan, FavouriteWorkoutSession, MuscleGroup, UserWorkoutPlan, WorkoutPlan, WorkoutSession
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import api_view
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

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Exercise.objects.all()
        else:
            return Exercise.objects.filter(public=True)
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


""" A to sie przyda tu 

              for index, workout_session in enumerate(workout_sessions):
                    day_date = start + timedelta(days=index)
                    UserWorkoutSession.objects.create(
                        workout_plan=user_workout_plan,
                        workout_session=workout_session,
                        date_of_workout=day_date)

Nad tym sie zastanowic tez czy moze nie powinno byc cos w tym stylu:
@login_required
def add_workout_plan_to_favourites(request, workout_plan_id):
    try:
        FavouriteWorkoutPlan.objects.get(
            workout_plan_id=workout_plan_id, user=request.user)
        return JsonResponse({'status': 'fail', 'message': _("This workout plan already is favourite")})
    except FavouriteWorkoutPlan.DoesNotExist:
        pass

    try:
        workout_plan = WorkoutPlan.objects.get(pk=workout_plan_id)
    except WorkoutPlan.DoesNotExist:
        return JsonResponse({'status': 'fail', 'message': _("This workout plan does not exist")})

    FavouriteWorkoutPlan.objects.create(
        workout_plan=workout_plan, user=request.user)
    return JsonResponse({'status': 'success'})


"""

class UserWorkoutPlanView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = UserWorkoutPlan.objects.all()
    serializer_class = USerWorkoutPlanSerializer


# @api_view(['POST'])


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