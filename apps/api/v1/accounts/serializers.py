from django.contrib.auth.models import User, Group
from rest_framework import serializers


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'is_staff', 'date_joined')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'date_joined')
