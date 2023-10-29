from django.contrib import admin

from .models import Order, OrderItem, ShippingAddress

admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)
