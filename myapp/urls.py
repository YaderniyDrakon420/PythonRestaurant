from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts', views.contacts),
    path('about', views.about),
    path('layout', views.layout),
    path('restaurant/delete/<int:restaurant_id>/', views.delete_restaurant, name='delete_restaurant'),
    path('restaurant/edit/<int:restaurant_id>/', views.edit_restaurant, name='edit_restaurant'),
    # path('category/<int:id>/', category),
    # path('category/<slug:category_slug>/', category)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)