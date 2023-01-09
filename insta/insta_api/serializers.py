from rest_framework import serializers
from .models import Photo, Comment, Like


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ["content", "time_added", "user", "username"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content", "created_at", "user_id", "photo_id"]


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["user_id", "photo_id"]