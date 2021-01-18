from django.contrib import messages
from django.shortcuts import render
from django.views import View
from cafeitems.models.menu_item import MenuItem


class Cart(View):

    def get(self, request):

        my_cart = request.session.get('cart')

        if not bool(my_cart):
            verify_cart_empty = False
            messages.info(request, "your list is empty")
            return render(request, 'cart.html', {'verify_cart_empty': verify_cart_empty})
        else:
            verify_cart_empty = True
            cart = list(my_cart.keys())
            cart_items = MenuItem.get_all_cart_item_by_id(cart)
            print(cart_items, cart)

            data = {'mycart': cart_items, 'verify_cart_empty': verify_cart_empty}

            return render(request, "cart.html", data)
