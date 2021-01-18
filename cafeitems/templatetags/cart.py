from django import template

register = template.Library()


# it will check if item is  available in cart
@register.filter(name='is_in_cart')
def is_in_cart(item, cart):
    cart_item_ids = cart.keys()
    for ids in cart_item_ids:
        if ids == 'null':
            return False
        else:
            if int(ids) == item.id:
                return True
    else:
        return False


# it will return the quantity of available item in cart
@register.filter(name='product_count')
def product_count(item, cart):
    cart_item_ids = cart.keys()

    for ids in cart_item_ids:

        if int(ids) == item.id:
            return cart.get(ids)


# it will return the price of available item in cart with respect of quantity
@register.filter(name='price_count')
def price_count(item, cart):

    return item.price * product_count(item, cart)


# it will return the total price of available item in cart
@register.filter(name='total_price_count')
def total_price_count(items, cart):
    total = 0

    for item in items:
        total += int(price_count(item, cart))

    return total


@register.filter(name='order_price_count')
def order_price_count(price, quantity):

    return price * quantity
