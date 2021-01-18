from django.contrib import messages
from django.shortcuts import render
from django.views import View
from cafeitems.models.orders import Order


class MyOrder(View):

    def get(self, request):

        if request.session.get('customer_email') is None:
            messages.info(request, "please signup first")
            return render(request, 'signup.html')

        customer = request.session.get('customer')
        order_item_list = Order.get_order_items_by_customer_id(customer)

        if not bool(order_item_list):
            messages.info(request, "your order list is empty")
            return render(request, 'myorder.html')

        else:

            return render(request, "myorder.html", {'myorders': order_item_list})
