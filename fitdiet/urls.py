from django.urls import path
from django.urls import include
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
router = routers.SimpleRouter()
router.register(r'Diet', views.DietView)
router.register(r'Meal', views.MealView)
router.register(r'UserDiet', views.UserDietView)
router.register(r'UserDietDay', views.UserDietDayView)
router.register(r'DietDay', views.DietDayView)
router.register(r'CookingStep', views.CookingStepView)
router.register(r'FavouriteMeal', views.FavouriteMealView)
router.register(r'FavouriteDiet', views.FavouriteDietView)


app_name = 'fitdiet'
urlpatterns = [
    path('usermeals/<int:pk>', views.user_exercises),
    path('diet_days_in_diet/<int:pk>', views.diet_days_in_diet)
]
