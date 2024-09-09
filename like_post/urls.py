from django.urls import path
from like_post import views

urlpatterns = [
    path('like_post/', views.LikePostList.as_view()),
    path('like_post/<int:pk>/', views.LikePostDetail.as_view()),
]