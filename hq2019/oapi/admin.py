from django.contrib import admin
from .models import Product, Popularity, Wishlist


# Register your models here.

@admin.register(Product)
class Product(admin.ModelAdmin):
    pass

@admin.register(Popularity)
class Popularity(admin.ModelAdmin):
    pass

@admin.register(Wishlist)
class Wishlist(admin.ModelAdmin):
    pass
