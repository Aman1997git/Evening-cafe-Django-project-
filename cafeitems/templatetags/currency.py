from django import template

register = template.Library()


# it will check if item is  available in cart
@register.filter(name='currency')
def currency(total):
    return str(total) + " Rs"
