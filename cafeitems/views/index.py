from django.views import View
from django.shortcuts import render, redirect
from cafeitems.models.menu_item import MenuItem
from cafeitems.models.menu import Menu


class Home(View):

    def get(self, request):

        # it will create a cart if cart is not already present
        cart = request.session.get('cart')

        if not cart:
            request.session.cart = {}
        # it will check category_id, it will serve item accordingly,
        # if category_id would be available otherwise it will serve all items
        category_id = request.GET.get('category')
        if category_id:
            products = MenuItem.get_all_menu_item_by_id(category_id)
        else:
            products = MenuItem.get_all_menu_item()

        data = {'items': products, 'category': Menu.get_all_menu_item()}
        return render(request, "home.html", data)

    def post(self, request):

        item_id = request.POST.get('item_id')
        remove_product = request.POST.get('remove_product')
        cart = request.session.get('cart')
        print('remove_product', item_id, cart)

        if cart:
            # it will remove item from cart
            if remove_product:

                # it will check the quantity of a particular items present in cart
                quantity = cart.get(item_id)

                # it will remove item from cart if would have only 1 quantity
                if quantity <= 1:
                    cart.pop(item_id)

                # Decrement quantity of item by 1
                else:
                    cart[item_id] = quantity - 1

            # it will add or item to cart
            else:

                # if item would be present in cart
                quantity = cart.get(item_id)
                if quantity:
                    cart[item_id] = quantity + 1
                    redirect('home')

                #  if item wouldn't be present in cart
                else:
                    cart[item_id] = 1
                    redirect('home')

        else:
            cart = {item_id: 1}
            request.session['cart'] = cart

        request.session['cart'] = cart
        print(cart)

        return redirect('home')

