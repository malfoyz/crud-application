from django.urls import path

from .views import (
    create_category, create_post, delete_category, delete_post,
    edit_category, edit_post, get_categories, get_post, index,
)


app_name = 'posts'
urlpatterns = [
    path('categories/delete/<int:id>/', delete_category, name='delete_category'),
    path('categories/edit/<int:id>/', edit_category, name='edit_category'),
    path('categories/create/', create_category, name='create_category'),
    path('categories/', get_categories, name='get_categories'),
    path('posts/delete/<int:id>/', delete_post, name='delete_post'),
    path('posts/edit/<int:id>/', edit_post, name='edit_post'),
    path('posts/create/', create_post, name='create_post'),
    path('posts/<int:id>/', get_post, name='get_post'),
    path('', index, name='home'),
]