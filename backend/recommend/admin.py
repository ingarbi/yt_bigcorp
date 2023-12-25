from django.contrib import admin

from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'rating', 'content', 'created_by', 'created_at')

admin.site.register(Review)
