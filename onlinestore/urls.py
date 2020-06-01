"""onlinestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from onlineapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contactus', views.contactus,name="contactus"),
    path('', views.home,name="home"),
    path('cart/', views.cart,name="cart"),
    path('checkout/', views.checkout,name="checkout"),
    path('shopgrid/', views.shopgrid,name="shopgrid"),
    path('register/', views.register,name="register"),
    path('suplier_regis/', views.suplier_register,name="suplier_regis"),
    path('admin_dashboard/',views.admin_dashboard,name="admin_dashboard"),
    path('loginus/', views.loginus,name="loginus"),
    path('cust_dashboard/', views.cust_dashboard,name="cust_dashboard"),
    path('blog/', views.blog,name="blog"),
    path('Membershipsbase/', views.Membershipsbase,name="Membershipsbase"),
    # path('g/', views.g,name="g"),
]