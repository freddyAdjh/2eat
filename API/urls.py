from django.urls import path,include
from .views import *

from rest_framework import routers


router = routers.DefaultRouter()
router.register('Shops',ShopViewSet,basename='Shops') 
router.register('Dish',DishViewSet,basename='Dish') 
router.register('location',LocationViewSet,basename='location') 
router.register('user',UserViewSet,basename='user') 
router.register('basket',BasketViewSet,basename='basket') 
router.register('order',OrderViewSet,basename='order')
router.register('addShop',AddShopViewSet,basename='addshops')

router.register('ratingmeal',RatingMealViewSet,basename='ratingmeal')
router.register('comment',CommentViewSet,basename='comment')
router.register('comment',CommentViewSet,basename='comment')


urlpatterns = [
    path('',include(router.urls)),
]