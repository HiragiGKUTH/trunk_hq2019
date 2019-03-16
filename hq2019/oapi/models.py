from django.db import models


class Product(models.Model):
    p_id = models.CharField(max_length=64);
    name = models.CharField(max_length=1024);
    price = models.IntegerField();
    img_url = models.CharField(max_length=1024, default="No Url")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Popularity(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    scan_count = models.IntegerField();

class Wishlist(models.Model):
    l_id = models.CharField(max_length=48);
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    persisted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.l_id