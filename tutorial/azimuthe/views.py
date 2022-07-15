from django.shortcuts import render

from azimuthe.models import Products, Warehouses
from rest_framework import viewsets
from azimuthe.serializers import ProductSerializer, WarehauseSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Products.objects.all().order_by('-prd_name')
    serializer_class = ProductSerializer


class WarehousesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Warehouses.objects.all().order_by('-whs_name')
    serializer_class = WarehauseSerializer

