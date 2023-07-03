from django.db import models

class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    
class ProductUser(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(unique=True)
    product_user = models.IntegerField(unique=True)
