from django.shortcuts import render


from rest_framework import viewsets,generics
from rest_framework.response import Response
from .models import * 
from .serializer import *
from rest_framework.parsers import MultiPartParser,FormParser

# Create your views here.


class ShopViewSet(viewsets.ModelViewSet):
    
    serializer_class = FoodShopSerializer

    def get_queryset(self):
        return FoodShop.objects.all()

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    parser_classes = (MultiPartParser,FormParser)


    def create(self, request, *args, **kwargs):
        name = request.data["name"]
        image = request.data["image"]

        Dish.objects.create(name=name,image=image)


        return Response("Food created successfully")
  
class LocationViewSet(viewsets.ModelViewSet):
    queryset = location.objects.all()
    serializer_class = LocationSerializer

class UserViewSet(viewsets.ModelViewSet):
    
    serializer_class = UserSerializer

    def get_queryset(self):
        return user.objects.all()
    
    def retrieve(self, request, *args, **kwargs):
        print(kwargs)
        return Response({})

    

class BasketViewSet(viewsets.ModelViewSet):
    queryset = basket.objects.all()
    serializer_class = BasketSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = order.objects.all()
    serializer_class = OrderSerializer

class AddShopViewSet(viewsets.ModelViewSet):
    queryset = AddShop.objects.all()
    serializer_class = AddShopSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = comments.objects.all()
    serializer_class = CommentSerializer

class RatingMealViewSet(viewsets.ModelViewSet):
    queryset = ratingMeal.objects.all()
    serializer_class = ratingMealSerializer
