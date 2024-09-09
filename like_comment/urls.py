from django.urls import path
from like_comment import views

urlpatterns = [
    path('like_comment/', views.LikeCommentList.as_view()),
    path('like_comment/<int:pk>/', views.LikeCommentDetail.as_view()),
]