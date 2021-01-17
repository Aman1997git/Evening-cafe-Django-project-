from django.contrib import admin
from .models.customer import Customer


class AdminCustomer(admin.ModelAdmin):
    list_display = ['name', 'username', 'email']


# Register your models here.
admin.site.register(Customer, AdminCustomer)