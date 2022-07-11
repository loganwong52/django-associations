from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20, default="")

class Post(models.Model):
    body = models.CharField(max_length=255, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", default="")

class Comment(models.Model):
    message = models.CharField(max_length=64, default="")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", default="")
