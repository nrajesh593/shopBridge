from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    productname = serializers.CharField(max_length=200)
    price = serializers.FloatField()
    description = serializers.CharField(required=False, default=1)
    image = serializers.CharField(max_length=5000)

    class Meta:
        model = Product
        fields = ('__all__')
