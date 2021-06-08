from rest_framework.views import APIView
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from knox.auth import AuthToken
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import status
from django.contrib.auth import logout,login


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = AuthToken.objects.create(user=user)[1]
        return Response({
            'token': token,
            'user': UserSerializer(user,context=self.get_serializer_context()).data
        })

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token = AuthToken.objects.create(user=user)[1]
        print("\n\n\n **************** \n")
        print(token)
        print("\n*********************\n")
        return Response({
            'token': token,
            'user': UserSerializer(user,context=self.get_serializer_context()).data
        })

class Logout(APIView):
    def post(self, request, format=None):
        # simply delete the token to force a login
        # For know knox and DRF are kinda not working when logging out. Unsolved issue
        print("\n\n\n **************** \n")
        print('REQUEST:', request.user)
        print("\n*********************\n")
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)