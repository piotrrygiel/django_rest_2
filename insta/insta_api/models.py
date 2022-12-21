from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    content = models.TextField()
    time_added = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.content


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    photo_id = models.ForeignKey(Photo, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.content


class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    photo_id = models.ForeignKey(Photo, on_delete=models.CASCADE, blank=True, null=True)


class Follow(models.Model):
    pass


class User(models.Model):
    pass
