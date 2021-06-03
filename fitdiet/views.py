from .serializers import CookingStepSerializer, DietDaySerializer, DietSerializer, MealSerializer,UserDietSerializer
from .models import CookingStep, Diet, DietDay, Meal, UserDiet
from rest_framework import mixins
from rest_framework import viewsets


# Create your views here.

class MealView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class DietView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer

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