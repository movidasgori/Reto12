"""api_bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapi.urls')),

    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),

    path('login/', include('rest_auth.registration.urls')),
    path('logout/', include('rest_auth.registration.urls')),
    path('user/', include('rest_auth.registration.urls')),
    path('password/chance/', include('rest_auth.registration.urls')),
    path('password/reset/', include('rest_auth.registration.urls')),
    path('password/resetconfirm/', include('rest_auth.registration.urls')),




]


