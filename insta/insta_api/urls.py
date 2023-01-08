from django.urls import path, include
from .views import(
    PhotoListApiView,
    CommentListApiView,
    CommentDetailApiView,
    LikeListApiView,
    LikeDetailApiView,
    homePageView
)

urlpatterns = [
    path('photos', PhotoListApiView.as_view()),
    path('comments', CommentListApiView.as_view()),
    path('comments/<int:photo_id>/', CommentDetailApiView.as_view()),
    path('likes', LikeListApiView.as_view()),
    path('likes/<int:photo_id>/', LikeDetailApiView.as_view()),
    path('homepage', homePageView, name="home")
]
