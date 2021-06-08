from rest_framework import mixins
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Measurement #, Profile
from .serializers import MeasurementSerializer, UserProfileSerializer #, ProfileSerializer
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

# class ProfileView(mixins.CreateModelMixin,
#                   mixins.ListModelMixin,
#                   mixins.DestroyModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.RetrieveModelMixin,
#                   viewsets.GenericViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

class MeasurementView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user']


class UserView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
