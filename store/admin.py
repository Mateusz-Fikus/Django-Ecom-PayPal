from django.contrib import admin
from .models import Items

@admin.register(Items)
class ItemAdmin(admin.ModelAdmin):
    list_display= ['name', 'desc', 'price', 'stock', 'image']