from django.urls import path

from . import views
from .webhooks import stripe_webhook, yookassa_webhook

app_name = 'payment'

urlpatterns = [
    path('payment-success/', views.payment_success, name='payment-success'),
    path('payment-failed/', views.payment_failed, name='payment-failed'),
    path('shipping/', views.shipping, name='shipping'),
    path('checkout/', views.checkout, name='checkout'),
    path('complete-order/', views.complete_order, name='complete-order'),
    path('webhook-stripe/', stripe_webhook, name='webhook-stripe'),
    path('webhook-yookassa/', yookassa_webhook, name='webhook-yookassa'),
    path("order/<int:order_id>/pdf/", views.admin_order_pdf, name="admin_order_pdf"),
]
