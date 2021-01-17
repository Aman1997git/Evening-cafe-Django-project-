from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=35)

    @staticmethod
    def get_all_menu_item():
        return Menu.objects.all()

    def __str__(self):
        return self.name


