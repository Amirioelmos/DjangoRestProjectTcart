from django.urls import path
from .api import RegisterApi, UserApi, UserUpdateApi, UserDeleteApi

urlpatterns = [
    path('api', UserApi.as_view()),
    path('api/register', RegisterApi.as_view()),
    path('api/<int:pk>', UserUpdateApi.as_view()),
    path('api/<int:pk>/delete', UserDeleteApi.as_view()),

]
