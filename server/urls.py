"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import re_path, path
from . import views

urlpatterns = [
    path('admin', admin.site.urls),
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('validate_answer', views.validate_answer),
    re_path('add_value', views.add_value),
    re_path('generate_task', views.generate_task),
    # Add more endpoints for other functionalities if needed
]
    