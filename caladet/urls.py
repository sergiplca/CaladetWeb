from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', views.APITweetList.as_view(), name='api'),
    path('api/new/', views.postAPI, name='postAPI'),
]