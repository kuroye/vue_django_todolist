from venv import create
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import UserSerializer, UserRegisterSerializer, CustomTokenObtainPairSerializer

from rest_framework_simplejwt.views import TokenObtainPairView

from .models import MyUser
# Create your views here.

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserCreateAPIView(generics.ListCreateAPIView):

    queryset = MyUser.objects.all()
    serializer_class = UserRegisterSerializer

    # def create(self, request, *args, **kwargs):
    #     data = super().create(request, *args, **kwargs)
    #     data['hello'] = 'hello world'

    #     print(data)
    #     return data 

 

class UserRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

class UserDoDoUpdateAPIView(APIView):

    def post(self, request):

        # print("IAM REQUEST DATA", request.data['dodo'])
        user_id = request.data['user_id']
        new_dodo = request.data['dodo']

        user = MyUser.objects.get(id=user_id)
        current_dodo = user.dodo
        sum_dodo = current_dodo + new_dodo

        user.dodo = sum_dodo

        user.save()

        return Response({'msg': 'ok lah',
                        'dodo': user.dodo,
                        'code':0}) 
