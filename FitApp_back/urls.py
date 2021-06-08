"""FitApp_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from main import api
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.urls import router as main_router
from workout.urls import router as workout_router
from fitdiet.urls import router as diet_router



router = routers.DefaultRouter()
router.registry.extend(main_router.registry)
router.registry.extend(workout_router.registry)
router.registry.extend(diet_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/register', api.RegisterAPI.as_view()),
    path('auth/login', api.LoginAPI.as_view()),
    path('auth/logout', api.Logout.as_view()),
    path('workout_plan_sessions/', include('workout.urls')),
    path('user_meals/', include('fitdiet.urls')),
    path('', include(router.urls)),
    # path('', include('workout.urls')),
    # path('diet/', include('fitdiet.urls')),
    # path('main/', include('main.urls'))
    # path('', include('fitdiet.urls'))
]
