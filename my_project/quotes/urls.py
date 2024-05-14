from django.urls import path
from . import views

app_name = "quotes"

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:page>', views.main, name='root_paginate'),
    path('add/', views.add, name='add'),
    path('about/<str:author_name>/', views.get_author, name='author'),
    path('add_author/', views.add_author, name='add_author'),
    path('tag/<str:tag_name>/', views.get_quotes_by_tag, name='tag'),
]
