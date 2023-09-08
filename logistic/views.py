from rest_framework import viewsets
from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer
from django_filters import rest_framework as django_filters

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [django_filters.DjangoFilterBackend]
    filterset_fields = ['title']  # Добавьте здесь поля для фильтрации

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [django_filters.DjangoFilterBackend]
    filterset_fields = ['address']  # Добавьте здесь поля для фильтрации
