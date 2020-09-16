from django.urls import path
from . import views

# app_name = 'app_store'

urlpatterns = [
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('insert_cart/',views.insert_into_cart,name='insert_cart'),
    path('cart/update_item/',views.update_item_quantity,name='update_item'),
    path('item_detail/<int:id>',views.item_detail,name='item_detail'),
]