from django.urls import path
from django.contrib import admin
from .views import *

app_name = 'board'

urlpatterns = [
     path('detail/<str:id>', detail, name='detail'),

     path('detail/<str:post_id>/comment', create_comment, name="create_comment"),
     path('detail/<str:post_id>/comment/<str:comment_id>', create_re_comment, name="re_comment"),

     path('like/', post_likes, name="post_likes"),

     path('', main, name='main'),
     path('category/<str:id>', category, name="category"),

     path('new/', new, name="new"),
     path('edit/<str:id>', edit, name="edit"),
     path('delete/<str:id>', delete, name="delete"),
     path('search/', search, name="search"),

 ] 