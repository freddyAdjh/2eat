from django.db import models

# Create your models here.



class Dish(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/food",)

    def __str__(self):
        return self.name

class location(models.Model):
    lat = models.DecimalField(max_digits=30,decimal_places=28)
    long = models.DecimalField(max_digits=30,decimal_places=28)
    class Meta:
        constraints = [
            models.UniqueConstraint(
            fields=['lat','long'],
            name='coordinate'
            )
        ]

class FoodShop(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    openinghour = models.CharField(max_length=5)
    closinghour = models.CharField(max_length=5)
    description = models.TextField()
    ownercontact = models.CharField(max_length=12)
    # solddish = models.ForeignKey(Dish,on_delete=models.CASCADE)
    location = models.ForeignKey(location,on_delete=models.CASCADE)
    saleprice = models.IntegerField()
    dish=models.ForeignKey(Dish,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
    
   



class user(models.Model):
    email = models.EmailField(primary_key=True)
    contact = models.CharField(max_length=13)
    role = models.IntegerField()


class AddShop(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    shop = models.ForeignKey(FoodShop,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False)

class basket(models.Model):
    owner = models.ForeignKey(user,on_delete=models.DO_NOTHING)

class order(models.Model):
    seasoning = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)
    quantity = models.IntegerField()
    date = models.DateField(auto_now_add=False)
    Basket = models.ForeignKey(basket,on_delete=models.CASCADE)
    meal = models.ForeignKey(Dish,on_delete=models.CASCADE)



class comments(models.Model):
    date = models.DateField(auto_now_add=False)
    comment = models.TextField()
    meal = models.ForeignKey(Dish,on_delete=models.CASCADE)
    user =  models.ForeignKey(user,on_delete=models.CASCADE)

class ratingMeal(models.Model):
    date = models.DateField(auto_now_add=False)
    point = models.DecimalField(max_digits=2,decimal_places=1)
    shop = models.ForeignKey(FoodShop,on_delete=models.CASCADE)
    user =  models.ForeignKey(user,on_delete=models.CASCADE)
