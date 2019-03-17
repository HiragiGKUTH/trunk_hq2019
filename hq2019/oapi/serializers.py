from rest_framework import serializers
from oapi.models import Product, Wishlist, Popularity


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("p_id", "name", "price", "img_url")

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"

class PopularitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Popularity
        fields = "__all__"