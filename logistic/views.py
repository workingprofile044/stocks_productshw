from rest_framework import viewsets, filters
from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer
from django_filters import rest_framework as django_filters
from rest_framework.pagination import PageNumberPagination

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'description']
    pagination_class = PageNumberPagination

class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['address']
    search_fields = ['products__title', 'products__description']
    pagination_class = PageNumberPagination
