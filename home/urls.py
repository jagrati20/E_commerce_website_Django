from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage, name='web_home'),
    path('shop/', views.shopping, name='shop_home'),
    path('checkout',views.checkout,name='checkout'),
    path('cart',views.cart,name='cart'),
    path('contact',views.contact,name='contact'),
    path('add-cart/<int:product_id>/', views.add_prods_cart, name='add_cart'),
    path('remove-cart/<int:product_id>/', views.remove_prods_cart, name='remove_cart')

]
