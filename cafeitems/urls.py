from django.urls import path
from .views.index import Home
from .views.cart import Cart
from .views.order import OrderView
from .views.myorder import MyOrder
from accounts.middlewares.auth_middleware import check_login_middleware

urlpatterns = [

    path('', Home.as_view(), name='home'),
    path('order', OrderView.as_view(), name='order'),
    path('myorder', check_login_middleware(MyOrder.as_view()), name='myorder'),
    path('cart', Cart.as_view(), name='cart')

]