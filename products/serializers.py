from rest_framework import serializers
from .models import Review, Product, ProductTag, FavoriteProduct, Cart, ProductImage

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'rating', 'product']  
    


class FavoriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProduct
        fields = ['id', 'product', 'user']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
  


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTag
        fields = "__all__"

 
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']
