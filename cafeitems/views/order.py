from django.contrib import messages
from django.views import View
from django.shortcuts import redirect, render

from accounts.models import Customer
from cafeitems.models import Order, Menu
from cafeitems.models.menu_item import MenuItem


class OrderView(View):

    def get(self, request):

        cart = request.session.get('cart')

        if request.session.get('customer_email') is None:
            messages.info(request, "please signup first")
            return render(request, 'signup.html')

        else:
            ids = list(request.session.get("cart").keys())
            items = MenuItem.get_all_cart_item_by_id(ids)
            name = request.session.get('customer')

            for product in items:

                orders = Order(
                    name=product.name,
                    customer=Customer(id=name),
                    price=product.price,
                    image=product.image,
                    quantity=cart.get(str(product.id)),
                    email=request.session.get('customer_email'),
                    category=Menu(id=product.category.id),
                )
                orders.save()
            request.session['cart'] = {}

        return redirect('myorder')
