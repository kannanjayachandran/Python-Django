from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('MyFirstApp/', include('MyFirstApp.urls')),
    path('admin/', admin.site.urls),
]
