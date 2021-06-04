from .serializers import CookingStepSerializer, DietDaySerializer, DietSerializer, FavouriteDietSerializer, FavouriteMealSerializer, MealSerializer,UserDietSerializer
from .models import CookingStep, Diet, DietDay, FavouriteDiet, FavouriteMeal, Meal, UserDiet
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import api_view

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

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Meal.objects.all()
        else:
            return Meal.objects.filter(public=True)

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


""" przyda się

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

    def get_queryset(self):
    #TODO: Mozliwe ze trzeba to zrobic zeby zwracalo posilki(bo teraz to moze byc klopotliwe po froncie)
        return FavouriteMeal.objects.filter(user=self.request.user)
        

class FavouriteDietView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = FavouriteDiet.objects.all()
    serializer_class = FavouriteDietSerializer

    def get_queryset(self):
    #TODO: Mozliwe ze trzeba to zrobic zeby zwracalo posilki(bo teraz to moze byc klopotliwe po froncie)
        return FavouriteDiet.objects.filter(user=self.request.user)