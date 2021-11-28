from django.contrib import admin
from .models import Item, Price


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_price', 'price_variation', 'display']
    search_fields = ('name',)
    list_filter = ('display',)


class PriceAdmin(admin.ModelAdmin):
    list_display = ['item', 'date', 'price']
    list_filter = ('item',)


admin.site.register(Item, ItemAdmin)
admin.site.register(Price, PriceAdmin)
