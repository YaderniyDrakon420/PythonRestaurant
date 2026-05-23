from django.db import models

class Specialization(models.Model):
    name = models.CharField(max_length=100)

class Restaurant(models.Model):
    title = models.CharField(max_length=50)
    specializations = models.ManyToManyField(Specialization)
    address = models.CharField(max_length=300)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=20)

class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='restaurants/')