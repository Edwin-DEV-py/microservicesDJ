from django.shortcuts import render
from .serializers import ProductSerializer
from rest_framework import viewsets

class ProductViewSet(viewsets.ViewSet):
    
    def list(self, request): #/api/products
        pass
        
    def create(self,request): #/api/products
        pass
    
    def retrieve(self, request, pk=None): #/api/products/<str:id>
        pass
    
    def update(self, request, pk=None): #/api/products/<str:id>
        pass
    
    def delete(self, request, pk=None): #/api/products/<str:id>
        pass
