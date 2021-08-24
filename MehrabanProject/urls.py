
from django.contrib import admin
from django.urls import path,include 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('',include('pwa.urls')),
    path('api/v1/',include('classes.urls')),
    path('classes/',include('classes.urls')),
]
