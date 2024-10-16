from django.urls import path
from .views import register_shop, shop_success, shop_search, nearby_shops, home

urlpatterns = [
    path('', home, name='home'),
    path('register/', register_shop, name='register_shop'),
    path('success/', shop_success, name='shop_success'),
    path('search/', shop_search, name='shop_search'),
    path('nearby/', nearby_shops, name='nearby_shops'),
]
