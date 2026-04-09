from django.urls import path
from .views import profiles, comments, add_comment, edit_comment, delete_comment

urlpatterns = [
    path('profiles/', profiles, name='profiles'),
    path('comments/', comments, name='comments'),
    path('comments/add/', add_comment, name='add_comment'),
    path('comments/<int:pk>/edit/', edit_comment, name='edit_comment'),
    path('comments/<int:pk>/delete/', delete_comment, name='delete_comment'),
]