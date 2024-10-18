"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views
from .models import Item
from users import views as user_views

# To namespace the urls and path for the particular app, we use app_name = "appname"
app_name = 'food'
urlpatterns = [
    path('', views.index, name="index"),
    # food/id
    path('<int:id>/', views.detail, name="detail"),
    path('addItem/', views.addItem, name="addItem"), #add item
    path('updateItem/<int:id>', views.updateItem, name="updateItem"), #updateItem
    path('deleteItem/<int:id>', views.deleteItem, name="deleteItem"), #deleteItem
    path('contact', views.contact, name="contact"),
    path('register/', user_views.register, name="userview"),
]
