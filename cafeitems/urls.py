from django.urls import path
from .views.index import Home
from .views.cart import Cart


urlpatterns = [

    path('', Home.as_view(), name='home'),
    path('cart', Cart.as_view(), name='cart')

]