"""task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls.conf import path, re_path, include
from django.contrib.auth.views import LogoutView
# from question.views import LoginView
from data.views import (
    AddDataView,
    GetDataView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', include(([
        path('get', GetDataView.as_view(), name='data_list'),
        path('add/', AddDataView.as_view(), name='add_data')
    ], 'task'), namespace='data')),
]
