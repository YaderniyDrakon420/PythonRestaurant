from django.contrib import admin
from django.urls import path, include
from myapp.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('staff/', include('staff.urls')),
]

handler404 = 'myapp.views.page_not_found'