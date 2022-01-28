from django.urls import path
from .views import *


urlpatterns = [
    path('api/firms/create',FirmsCreateApi.as_view()),
    path('api/products/create',ProductsCreateApi.as_view()),
    path('api/sales/create',SalesCreateApi.as_view()),

    path('api/firms/reed',FirmsApi.as_view()),
    path('api/products/reed',ProductsApi.as_view()),
    path('api/sales/reed',SalesApi.as_view()),

    path('api/firms/<int:pk>',FirmsUpdateApi.as_view()),
    path('api/products/<int:pk>',ProductsUpdateApi.as_view()),
    path('api/sales/<int:pk>',SalesUpdateApi.as_view()),

    path('api/firms/delete/<int:pk>',FirmsDeleteApi.as_view()),
    path('api/Products/delete/<int:pk>',ProductsDeleteApi.as_view()),
    path('api/Sales/delete/<int:pk>',SalesDeleteApi.as_view()),
]