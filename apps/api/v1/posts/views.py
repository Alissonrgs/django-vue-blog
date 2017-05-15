from rest_framework import generics
from .serializers import PostSerializer, CommentSerializer
from apps.blog.models import Post, Comment


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
