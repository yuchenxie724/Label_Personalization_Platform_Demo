"""development URL Configuration

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
from django.urls import path

from users.views import profile_info, login_page, add_function, delete_function, rename_function

urlpatterns = [
    path('', login_page, name = "index"),
    path('admin/', admin.site.urls),
    path('add/', add_function, name = "add"),
    path('delete/', delete_function, name = "delete"),
    path('rename/', rename_function, name = "rename")
    

]

