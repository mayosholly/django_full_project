from django.urls import path
from .views import PostCreateView
from .views import PostListView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/edit', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]