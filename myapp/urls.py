from django.urls import path
from .views import index, category

urlpatterns = [
    path('', index, name='main'),
    path('category/<int:id>/', category),
    path('category/<slug:category_slug>/', category)
]