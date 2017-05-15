from rest_framework import serializers
from apps.blog.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('author', 'liked', 'description', 'status', 'posted')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('post', 'author', 'liked', 'description', 'status', 'posted')
