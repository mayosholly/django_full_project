from django.urls import path
from .views import CategoryListView
from .views import CategoryCreateView
from .views import CategoryUpdateView
from .views import CategoryDeleteView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_add'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/destroy', CategoryDeleteView.as_view(), name='category_destroy'),
]