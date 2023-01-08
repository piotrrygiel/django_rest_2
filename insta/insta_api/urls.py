from django.urls import path, include
from .views import(
    PhotoListApiView,
    PhotoDetailApiView,
    CommentListApiView,
    CommentDetailApiView,
    LikeListApiView,
    LikeDetailApiView,
    FollowListApiView,
    FollowDetailedApiView,
    homePageView
)

urlpatterns = [
    path('photos', PhotoListApiView.as_view()),
    path('photos/<int:photo_id>/', PhotoDetailApiView.as_view()),
    path('photos/<int:photo_id>/comments', CommentListApiView.as_view()),
    path('photos/<int:photo_id>/likes', LikeListApiView.as_view()),
    path('comments/<int:comment_id>/', CommentDetailApiView.as_view()),
    path('likes/<int:like_id>/', LikeDetailApiView.as_view()),
    path('users/<int:following_id>/followers', FollowListApiView.as_view()),
    path('follows/<int:follow_id>/', FollowDetailedApiView.as_view()),
    path('homepage', homePageView, name="home")
]
