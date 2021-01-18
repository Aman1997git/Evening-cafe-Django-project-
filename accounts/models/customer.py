from datetime import datetime
from django.db import models


class Customer(models.Model):

    username = models.CharField(max_length=35)
    name = models.CharField(max_length=35)
    email = models.EmailField(max_length=35)
    password = models.CharField(max_length=35)
    date = models.DateField(default=datetime.today)

    @staticmethod
    def get_customer_by_email(email):
        return Customer.objects.get(email=email)

    def __str__(self):
        return self.email

    def register(self):
        return self.save()


