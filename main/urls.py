from django.urls import path
from django.urls import include
from rest_framework import routers
from . import views
from . import api

router = routers.DefaultRouter()
router.register(r'measurement', views.MeasurementView)


app_name = 'main'
urlpatterns = [
    path('', include(router.urls)),
    path('auth/register', api.RegisterAPI.as_view()),
    path('auth/login', api.LoginAPI.as_view()),
    path('auth/logout', api.Logout.as_view()),
]
