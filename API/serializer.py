from rest_framework import serializers
from .models import *


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('__all__')

class FoodShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodShop
        fields = ('__all__')
        

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = location
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('__all__')

class AddShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddShop
        fields = ('__all__')

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = basket
        fields = ('__all__')
  

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comments
        fields = ('__all__')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = order
        fields = ('__all__')


class ratingMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = ratingMeal
        fields = ('__all__')

