"""
URL configuration for ecart_project project.

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
from django.urls import path
from ecart_app import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('signin',views.Signin,name='signin'),
    path('register',views.Register,name="register"),
    path('category',views.Category,name="category"),
    path('subcategory/<int:id>',views.Subcategory,name="subcategory"),
    path('product/<int:id>',views.Product,name="product"),
    path('viewproduct/<int:id>',views.Viewproduct,name="viewproduct"),
    path('order/<int:id>',views.Order,name="order"),
    path('orders/<int:id>',views.Orders,name="orders"),
    path('buy',views.Buy,name="buy"),
    path('cancelorder/<int:id>',views.Cancelorder,name="cancelorder"),
    path('remove/<int:id>',views.Remove,name="remove"),
    path('cart/<int:id>',views.Cart,name="cart"),
    path('carts',views.Carts,name="carts"),
    path('removecart/<int:id>',views.removecart,name="removecart"),
    path('signout',views.Signout,name="signout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
