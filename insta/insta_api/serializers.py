from rest_framework import serializers
from .models import Photo, Comment, Like, Follow


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
        fields = ["user_id", "photo_id", "id"]


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ["follower_id", "following_id", "id"]