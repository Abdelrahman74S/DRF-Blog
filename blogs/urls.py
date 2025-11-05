# blogs/urls.py

from django.urls import path
from . import views

urlpatterns = [

    path('posts/', views.PostListCreateView.as_view(), name='post-list-create'),

    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),

    path('posts/<int:post_pk>/comments/', views.CommentListCreateView.as_view(), name='comment-list-create'),
    
    path('posts/<int:post_pk>/comments/<int:pk>/', views.CommentDetailView.as_view(), name='comment-detail')
]