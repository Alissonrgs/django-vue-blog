from django.contrib.auth.models import User
from apps.blog.models import Post, Comment
from rest_framework import generics
from .serializers import UserListSerializer, UserCreateSerializer,\
                         PostSerializer, CommentSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.filter(status=True).order_by('-posted')
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.filter(status=True).order_by('-posted')
    serializer_class = CommentSerializer


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.filter(status=True)
    serializer_class = CommentSerializer
