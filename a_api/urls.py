from django.urls import path
from .views import *

urlpatterns = [
    path('', profiles),
    path('comments/add/', add_comment),
    path('comments/', comments) 
]