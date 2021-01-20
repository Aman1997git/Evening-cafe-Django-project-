from django.contrib import messages
from django.shortcuts import render
from django.views import View
from cafeitems.models.orders import Order


class MyOrder(View):

    # Middleware "auth_middleware" will check whether user is logged in or not before handling "myOrder" method

    def get(self, request):

        customer = request.session.get('customer')
        order_item_list = Order.get_order_items_by_customer_id(customer)

        if not bool(order_item_list):
            messages.info(request, "your order list is empty")
            return render(request, 'myorder.html')

        else:

            return render(request, "myorder.html", {'myorders': order_item_list})
