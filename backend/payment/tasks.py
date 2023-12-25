from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from .models import Order, ShippingAddress


@shared_task()
def send_order_confirmation(order_id):
    
    order = Order.objects.get(id=order_id)
    subject = f'Order {order.id} payment Confirmation'
    receipent_data = ShippingAddress.objects.get(user=order.user)
    receipent_email = receipent_data.email
    message = f'Your order and payment has been confirmed. Your order number is {order.id}.'

    mail_to_sender = send_mail(
        subject,message=message,from_email=settings.EMAIL_HOST_USER, recipient_list=[receipent_email],
    )
    return mail_to_sender