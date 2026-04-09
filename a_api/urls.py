from django.urls import path
from .views import profiles, comments, add_comment

urlpatterns = [
    path('profiles/', profiles, name='profiles'),
    path('comments/', comments, name='comments'),
    path('comments/add/', add_comment, name='add_comment'),
]