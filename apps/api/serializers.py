from django.contrib.auth.models import User
from rest_framework import serializers
from apps.blog.models import Post, Comment


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'is_staff', 'date_joined')


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'date_joined')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('author', 'liked', 'description', 'status', 'posted')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('post', 'author', 'liked', 'description', 'status', 'posted')
