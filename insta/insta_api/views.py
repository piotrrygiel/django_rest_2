from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.db.models import Q
# from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Photo, Comment, Like, Follow
from .serializers import PhotoSerializer, CommentSerializer, LikeSerializer, FollowSerializer


class PhotoListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        insta_posts = Photo.objects
        serializer = PhotoSerializer(insta_posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'content': request.data.get('content'),
            'user': request.user.id,
            'username': request.user.username
        }
        serializer = PhotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhotoDetailApiView(APIView):
    permision_classes = [permissions.IsAuthenticated]

    def get(self, request, photo_id, *args, **kwargs):
        try:
            photo_instance = Photo.objects.get(id=photo_id)
        except Photo.DoesNotExist:
            return Response(
                {"res": "Photo with photo_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PhotoSerializer(photo_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, photo_id, *args, **kwargs):
        try:
            photo_instance = Photo.objects.get(id=photo_id, user=request.user.id)
        except Photo.DoesNotExist:
            return Response(
                {"res": "Photo with photo_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'content': request.data.get('content'),
            'user': request.user.id,
            'username': request.user.username
        }
        serializer = PhotoSerializer(instance=photo_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, photo_id, *args, **kwargs):
        try:
            photo_instance = Photo.objects.get(id=photo_id, user=request.user.id)
        except Photo.DoesNotExist:
            return Response(
                {"res": "Photo with photo_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        photo_instance.delete()
        return Response(
            {"res": "Photo deleted!"},
            status=status.HTTP_200_OK
        )


class CommentListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, photo_id, *args, **kwargs):
        # returns all comments under photo with given photo_id
        comments_instance = Comment.objects.filter(photo_id=photo_id)
        if not comments_instance:
            return Response(
                {"res": "Comments with photo_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CommentSerializer(comments_instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, photo_id, *args, **kwargs):
        data = {
            'content': request.data.get('content'),
            'user_id': request.user.id,
            'photo_id': photo_id
        }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, comment_id, *args, **kwargs):
        try:
            comment_instance = Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            return Response(
                {"res": "Comment with comment_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CommentSerializer(comment_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, comment_id, *args, **kwargs):
        # updates conent of comment with given comment_id
        try:
            comment_instance = Comment.objects.get(id=comment_id, user_id=request.user.id)
        except Comment.DoesNotExist:
            return Response(
                {"res": "Comment with comment_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'content': request.data.get('content'),
            'user_id': request.user.id,
        }
        serializer = CommentSerializer(instance=comment_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id, *args, **kwargs):
        try:
            comment_instance = Comment.objects.get(id=comment_id, user_id=request.user.id)
        except Comment.DoesNotExist:
            return Response(
                {"res": "Comment with comment_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        comment_instance.delete()
        return Response(
            {"res": "Comment deleted!"},
            status=status.HTTP_200_OK
        )

class LikeListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, photo_id, *args, **kwargs):
        likes_instance = Like.objects.filter(photo_id=photo_id)
        if not likes_instance:
            return Response(
                {"res": "Object with photo_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = LikeSerializer(likes_instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, photo_id, *args, **kwargs):
        data = {
            'user_id': request.user.id,
            'photo_id': photo_id
        }
        check = Like.objects.filter(Q(user_id=request.user.id) & Q(photo_id=photo_id))
        if check.exists():
            return Response(
                {"res": "Already liked"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = LikeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, like_id, *args, **kwargs):
        try:
            like_instance = Like.objects.get(id=like_id, user_id=request.user.id)
        except Like.DoesNotExist:
            return Response(
                {"res": "Like with like_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        like_instance.delete()
        return Response(
            {"res": "Like deleted!"},
            status=status.HTTP_200_OK
        )


class FollowListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, following_id, *args, **kwargs):
        follows_instance = Follow.objects.filter(following_id=following_id)
        if not follows_instance:
            return Response(
                {"res": "Object with following_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = FollowSerializer(follows_instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, following_id, *args, **kwargs):
        data = {
            'follower_id': request.user.id,
            'following_id': following_id
        }
        check = Follow.objects.filter(Q(follower_id=request.user.id) & Q(following_id=following_id))
        if check.exists():
            return Response(
                {"res": "You already follow this user"},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer = FollowSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FollowDetailedApiView(APIView):
    def delete(self, request, follow_id, *args, **kwargs):
        try:
            follow_instance = Follow.objects.get(id=follow_id, follower_id=request.user.id)
        except Follow.DoesNotExist:
            return Response(
                {"res": "Follow with follow_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        follow_instance.delete()
        return Response(
            {"res": "Follow deleted!"},
            status=status.HTTP_200_OK
        )

# def homePageView(request):
#     return HttpResponse(Like.objects.filter(photo_id=3).count())

def homePageView(request):
    likes_counter = Like.objects.filter(photo_id=3).count()
    context = {
        'likes_counter': likes_counter
    }

    return render(request, 'home.html', context=context)
