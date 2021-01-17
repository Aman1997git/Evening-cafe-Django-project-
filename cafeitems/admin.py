from django.contrib import admin
from cafeitems.models.menu import Menu
from cafeitems.models.menu_item import MenuItem


class AdminMenu(admin.ModelAdmin):
    list_display = ['name']


class AdminMenuItem(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


# Register your models here.
admin.site.register(Menu, AdminMenu)
admin.site.register(MenuItem, AdminMenuItem)