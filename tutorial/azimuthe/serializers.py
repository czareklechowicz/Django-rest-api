from azimuthe.models import Products, Warehouses
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Products
        fields = ['url', 'prd_name', 'prd_created', 'prd_warehause']


class WarehouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Warehouses
        fields = ['url', 'whs_name','whs_address']