from rest_framework import serializers
from oapi.models import Product, Wishlist


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("p_id", "name", "price")

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        return validated_data