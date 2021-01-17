from django.shortcuts import render
from django.views import View
from cafeitems.models.menu_item import MenuItem


class Cart(View):

    def get(self, requests):
        my_cart = requests.session.get('cart')

        if not bool(my_cart):
            pass
        else:
            cart = list(my_cart.keys())
            cart_items = MenuItem.get_all_cart_item_by_id(cart)
            print(cart_items, cart, list(cart))
            return render(requests, "cart.html", {'mycart': cart_items})
