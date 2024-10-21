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
from users import views as user_views #importing views directly from users app
from . import settings
# inbuilt views for login and logout functionality
from django.contrib.auth import views as authViews
from django.contrib.auth import logout
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/', include('food.urls')),
    path('register/', user_views.register, name="register"),

    # Login and logout are class based views and to use class based views, we have to use as_view() with name
    #ALthough we dont have to create views specifially for login and logout, but still we have to 
    #create a template for them. So we have to spcecify that where we are creating those templates. So
    #we pass that path info inside as_view as paramater
    path('login/', authViews.LoginView.as_view(template_name='users/login.html'), name="login"),
    # path('logout/', authViews.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('logout/', user_views.custom_logout, name='logout'),
    path('profile/', user_views.profilepage, name="profile"),
]

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)