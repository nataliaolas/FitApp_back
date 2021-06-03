from django.urls import path
from django.urls import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Diet', views.DietView)
router.register(r'Meal', views.MealView)
router.register(r'UserDiet', views.UserDietView)
router.register(r'DietDay', views.DietDayView)
router.register(r'CookingStep', views.CookingStepView)



app_name = 'fitdiet'
urlpatterns = [
    path('', include(router.urls)),
]
