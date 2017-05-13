from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts')
    liked = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    description = models.TextField()
    status = models.BooleanField(default=True)
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User, related_name='comments')
    liked = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    description = models.TextField()
    status = models.BooleanField(default=True)
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
