from django.urls import path

from product.api import ProductApi, ProductUpdateApi, ProductCreateApi, ProductDeleteApi

urlpatterns = [
    path('api', ProductApi.as_view()),
    path('api/create', ProductCreateApi.as_view()),
    path('api/<int:pk>', ProductUpdateApi.as_view()),
    path('api/<int:pk>/delete', ProductDeleteApi.as_view()),
]
