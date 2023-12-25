from django.urls import path
from .views import cart_view, cart_add, cart_delete, cart_update



app_name = 'cart'

urlpatterns = [
    path('', cart_view, name='cart-view'),
    path('add/', cart_add, name='add-to-cart'),
    path('delete/', cart_delete, name='delete-to-cart'),
    path('update/', cart_update, name='update-to-cart'),
    
]