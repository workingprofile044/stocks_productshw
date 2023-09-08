from rest_framework import serializers
from .models import Product, Stock, StockProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class StockProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = '__all__'

class StockSerializer(serializers.ModelSerializer):
    positions = StockProductSerializer(many=True, read_only=True)

    class Meta:
        model = Stock
        fields = '__all__'

    def create(self, validated_data):
        positions_data = validated_data.pop('positions', [])

        stock = Stock.objects.create(**validated_data)

        for position_data in positions_data:
            StockProduct.objects.create(stock=stock, **position_data)

        return stock

    def update(self, instance, validated_data):
        positions_data = validated_data.pop('positions', [])

        StockProduct.objects.filter(stock=instance).delete()

        for position_data in positions_data:
            StockProduct.objects.create(stock=instance, **position_data)

        return instance
