from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    restaurants = models.ManyToManyField('myapp.Restaurant', related_name='owners')

class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    position = models.CharField(max_length=100, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()
    restaurant = models.ForeignKey('myapp.Restaurant', on_delete=models.CASCADE, related_name='employees')