from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ProductSerializer
from rest_framework import viewsets
from .models import Product


class ProductViewSet(viewsets.ViewSet):
    
    def list(self, request): #/api/products
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
        
