from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('article/new/', views.article_new, name='article_new'),
]