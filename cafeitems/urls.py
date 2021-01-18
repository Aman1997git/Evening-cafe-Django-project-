from django.urls import path
from .views.index import Home
from .views.cart import Cart
from .views.order import OrderView
from .views.myorder import MyOrder

urlpatterns = [

    path('', Home.as_view(), name='home'),
    path('order', OrderView.as_view(), name='order'),
    path('myorder', MyOrder.as_view(), name='myorder'),
    path('cart', Cart.as_view(), name='cart')

]