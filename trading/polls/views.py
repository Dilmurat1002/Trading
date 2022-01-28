
from rest_framework import generics
from .models import *
from .serializers import FirmsSerializers, ProductsSerializers, SalesSerializers
# Create your views here.

"""Create"""
class FirmsCreateApi(generics.CreateAPIView):
    queryset = Firms.objects.all()
    serializer_class = FirmsSerializers

class ProductsCreateApi(generics.CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers

class SalesCreateApi(generics.CreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializers


"""READ"""
class FirmsApi(generics.ListAPIView):
    queryset = Firms.objects.all()
    serializer_class = FirmsSerializers

class ProductsApi(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers

class SalesApi(generics.ListAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializers


"""UPDATE"""
class FirmsUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Firms.objects.all()
    serializer_class = FirmsSerializers

class ProductsUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers

class SalesUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializers


"""DELETE"""
class FirmsDeleteApi(generics.DestroyAPIView):
    queryset = Firms.objects.all()
    serializer_class = FirmsSerializers

class ProductsDeleteApi(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializers

class SalesDeleteApi(generics.DestroyAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializers



