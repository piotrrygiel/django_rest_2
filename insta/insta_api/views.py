from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
# from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Photo, Comment, Like
from .serializers import PhotoSerializer, CommentSerializer, LikeSerializer


class PhotoListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        insta_posts = Photo.objects.filter(user=request.user.id)
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


class CommentListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        comments = Comment.objects.filter(user_id=request.user.id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'content': request.data.get('content'),
            'user_id': request.user.id,
            'photo_id': request.data.get('photo_id')
        }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    '''
    def get_comments(self, photo_id):

        Helper method to get the objects (comments) with given photo_id

        try:
            return Comment.objects.filter(photo_id=photo_id)
        except Comment.DoesNotExist:
            return None
    '''

    def get(self, request, photo_id, *args, **kwargs):
        comments_instance = Comment.objects.filter(photo_id=photo_id)
        if not comments_instance:
            return Response(
                {"res": "Object with photo_id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CommentSerializer(comments_instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LikeListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = {
            'user_id': request.user.id,
            'photo_id': request.data.get('photo_id')
        }
        serializer = LikeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LikeDetailApiView(APIView):
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


# def homePageView(request):
#     return HttpResponse(Like.objects.filter(photo_id=3).count())

def homePageView(request):
    likes_counter = Like.objects.filter(photo_id=3).count()
    context = {
        'likes_counter': likes_counter
    }

    return render(request, 'home.html', context=context)
