from django.db import models


class Product(models.Model):
    p_id = models.CharField(max_length=64);
    name = models.CharField(max_length=1024);
    price = models.IntegerField();
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Popularity(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    scan_count = models.IntegerField();

class Wishlist(models.Model):
    l_id = models.CharField(max_length=48);
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)