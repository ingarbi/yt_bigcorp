import csv
import datetime

from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Order, OrderItem, ShippingAddress


def export_paid_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f"attachment; filename=Paid{opts.verbose_name}.csv"
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = content_disposition
    writer = csv.writer(response)
    fields = [
        field
        for field in opts.get_fields()
        if not field.many_to_many and not field.one_to_many 
    ]
    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
        if not getattr(obj, "paid"):
            continue
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime("%d/%m/%Y")
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_paid_to_csv.short_description = "Export Paid to CSV"

def export_not_paid_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f"attachment; filename=NotPaid{opts.verbose_name}.csv"
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = content_disposition
    writer = csv.writer(response)
    fields = [
        field
        for field in opts.get_fields()
        if not field.many_to_many and not field.one_to_many 
    ]
    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
        if getattr(obj, "paid"):
            continue
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime("%d/%m/%Y")
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_not_paid_to_csv.short_description = "Export Not Paid to CSV"

def order_pdf(obj):
    url = reverse('payment:admin_order_pdf', args=[obj.id])
    return mark_safe(f'<a href="{url}">PDF</a>')

order_pdf.short_description = 'Invoice'

class ShippingAdressAdmin(admin.ModelAdmin):
    list_display = ('full_name_bold','user', 'email', 'country', 'city', 'zip')
    empty_value_display = "-empty-"
    list_display_links = ('full_name_bold',)
    list_filter = ('user', 'country', 'city')

    @admin.display(description="Full Name", empty_value="Noname")
    def full_name_bold(self, obj):
        return format_html("<b style='font-weight: bold;'>{}</b>", obj.full_name)
    
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['price', 'product', "quantity", "user"]
        return super().get_readonly_fields(request, obj)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'shipping_address', 'amount',
                    'created', 'updated', 'paid', 'discount', order_pdf
]
    list_filter = ['paid', 'updated','created',]
    inlines = [OrderItemInline]
    list_per_page = 15
    list_display_links = ['id', 'user']
    actions = [export_paid_to_csv, export_not_paid_to_csv]

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress, ShippingAdressAdmin)


