from django.contrib import admin
from .models import Specialization, Restaurant, RestaurantImage, Review

admin.site.register(Specialization)
admin.site.register(Restaurant)
admin.site.register(RestaurantImage)
admin.site.register(Review)