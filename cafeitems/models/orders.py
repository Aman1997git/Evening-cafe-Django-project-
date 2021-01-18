from django.db import models
from accounts.models.customer import Customer
from cafeitems.models.menu import Menu
from datetime import datetime


class Order(models.Model):
    name = models.CharField(max_length=40, default='None')
    email = models.EmailField(max_length=40)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Menu, on_delete=models.CASCADE, default=1)
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='uploaded_images/', default='Not available')
    date = models.DateField(default=datetime.today)
    status = models.BooleanField(default=False)

    @staticmethod
    def get_order_items_by_customer_id(customer):
        return Order\
            .objects\
            .filter(customer_id=customer).order_by('-date')

    def __str__(self):
        return str(self.customer)

    def saveorder(self):
        return self.save()

