from rest_framework import serializers
from .models import Firms, Products, Sales

class FirmsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Firms
        fields = "__all__"

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"

class SalesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = "__all__"