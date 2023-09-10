from dataclasses import field
from rest_framework import serializers
from .models import MyUser

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        data['user'] = UserSerializer(self.user).data
        data['code'] = 0
        

        return data

class Create_token(TokenObtainPairSerializer):
    def validate(self, user):
        refresh = self.get_token(user)
        data = {"user_id": user.id, "token": str(refresh.access_token), "refresh": str(refresh)}
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
         
class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = '__all__'

    def create(self, validated_data):
        user = super().create(validated_data)

        user.set_password(validated_data['password'])
        user.save()

        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['token'] = Create_token().validate(instance)
        return data