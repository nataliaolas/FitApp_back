from .serializers import CookingStepSerializer, DietDaySerializer, DietDayWithMealNamesSerializer, DietSerializer, FavouriteDietSerializer, FavouriteMealSerializer, MealSerializer, UserDietDaySerializer,UserDietSerializer
from .models import CookingStep, Diet, DietDay, FavouriteDiet, FavouriteMeal, Meal, UserDiet, UserDietDay
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
import datetime
# Create your views here.

class MealView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]


@api_view(['GET'])
def user_exercises(request,pk):
    if request.method == 'GET':
        meal = Meal.objects.filter(author=pk)
        serializer = MealSerializer(meal,many=True)
        return Response(serializer.data)
    return Response("Cos nie pyklo")

@api_view(['GET'])
def user_favdiets(request,pk):
    if request.method == 'GET':
        user_diets = FavouriteDiet.objects.filter(user=pk)
        serializer = FavouriteDietSerializer(user_diets,many=True)
        return Response(serializer.data)
    return Response("Cos nie pyklo")

@api_view(['GET'])
def diet_days_in_diet(request,pk):
    if request.method == 'GET':
        diet = Diet.objects.get(id=pk)
        diet_days = diet.diet_days
        serializer = DietDaySerializer(diet_days,many=True)
        return Response(serializer.data)
    return Response("Cos nie pyklo")

@api_view(['GET'])
def current_diet(request,pk):
    if request.method == 'GET':
        diet = UserDiet.objects.get(id=pk)
        now = datetime.datetime.now()
        diet_day = Diet.objects.get(diet=diet)
        if diet_day:
            serializer = UserDietDaySerializer(diet_day)
        else:
            return Response("Nie ma dzisiaj diety.")
        return Response(serializer.data)
    return Response("Cos nie pyklo")





class DietView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]


""" przyda si??

            if duration <= diet.duration_in_days:
                diet_days = diet.diet_days.all()[:duration]
                for index, day in enumerate(diet_days):
                    day_date = start + timedelta(days=index)
                    UserDietDay.objects.create(
                        diet=user_diet, diet_day=day, diet_day_date=day_date)

 """
class UserDietView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = UserDiet.objects.all()
    serializer_class = UserDietSerializer

class UserDietDayView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = UserDietDay.objects.all()
    serializer_class = UserDietDaySerializer

class DietDayView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = DietDay.objects.all()
    serializer_class = DietDaySerializer

class CookingStepView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = CookingStep.objects.all()
    serializer_class = CookingStepSerializer

class FavouriteMealView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = FavouriteMeal.objects.all()
    serializer_class = FavouriteMealSerializer

    filter_backends = [DjangoFilterBackend]
    search_fields = ['user',]
        

class FavouriteDietView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = FavouriteDiet.objects.all()
    serializer_class = FavouriteDietSerializer

    filter_backends = [DjangoFilterBackend]
    search_fields = ['user',]

class DietDayWithMealsNamesView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = DietDay.objects.all()
    serializer_class = DietDayWithMealNamesSerializer


@api_view(['GET'])
def user_fav_meal_view(request,pk):
    if request.method == 'GET':
        user_favourites = FavouriteMeal.objects.filter(user=pk)
        fav_exercises_id_list = []
        for i in user_favourites:
            fav_exercises_id_list.append(i.meal.id)
        filtered_list = Meal.objects.filter(id__in=fav_exercises_id_list)
        serializer = MealSerializer(filtered_list,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def user_fav_diet_view(request,pk):
    if request.method == 'GET':
        user_favourites = FavouriteDiet.objects.filter(user=pk)
        fav_exercises_id_list = []
        for i in user_favourites:
            fav_exercises_id_list.append(i.diet.id)
        filtered_list = Diet.objects.filter(id__in=fav_exercises_id_list)
        serializer = DietSerializer(filtered_list,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def current_diet_day(request,pk):
    if request.method == 'GET':
        # now = datetime.datetime.now()
        # diet = UserDiet.objects.filter(user=pk, start_date=now)
        try:
            now = datetime.datetime.now()
            diet = UserDiet.objects.filter(user=pk, start_date=now)
        except:
            print("COS NIE PYKLO HALO HALO")
            return Response("Cos nie pyklo")
        else:
            current_diet = 0
            for i in range(len(diet)):
                if i == len(diet)-1:
                    current_diet = diet[i].diet
            print(current_diet)
            diet_days = current_diet.diet_days
            serializer = DietDaySerializer(diet_days,many=True)
            print("""\n\n\n SUCCUESS \n\n """)
            return Response(serializer.data)
    return Response("Cos nie pyklo")



#     @api_view(['GET'])
# def diet_days_in_diet(request,pk):
#     if request.method == 'GET':
#         diet = Diet.objects.get(id=pk)
#         diet_days = diet.diet_days
#         serializer = DietDaySerializer(diet_days,many=True)
#         return Response(serializer.data)
#     return Response("Cos nie pyklo")