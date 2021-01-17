from django.db import models
from cafeitems.models.menu import Menu


class MenuItem(models.Model):
    name = models.CharField(max_length=35)
    image = models.ImageField(upload_to='uploaded_images/')
    price = models.IntegerField(default=0.00)
    category = models.ForeignKey(Menu, on_delete=models.CASCADE, default='category not avialable')

    @staticmethod
    def get_all_menu_item():
        return MenuItem.objects.all()

    @staticmethod
    def get_all_menu_item_by_id(category_id):
        return MenuItem.objects.filter(category_id=category_id)

    @staticmethod
    def get_all_cart_item_by_id(ids):
        return MenuItem.objects.filter(id__in=ids)

    @staticmethod
    def get_all_menu_item_by_item_id(item_id):
        item = MenuItem.objects.filter(id=item_id)
        if item:
            return True
        else:
            False

    def __str__(self):
        return self.name

