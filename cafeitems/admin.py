from django.contrib import admin
from cafeitems.models.menu import Menu
from cafeitems.models.menu_item import MenuItem
from cafeitems.models.orders import Order


class AdminMenu(admin.ModelAdmin):
    list_display = ['name']


class AdminMenuItem(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminOrder(admin.ModelAdmin):
    list_display = ['name', 'customer', 'date', 'category']


# Register your models here.
admin.site.register(Menu, AdminMenu)
admin.site.register(MenuItem, AdminMenuItem)
admin.site.register(Order, AdminOrder)