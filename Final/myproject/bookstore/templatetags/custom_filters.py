from django import template

register = template.Library()

@register.filter
def get_item_count(cart, book_id):
    return cart.get(str(book_id), 0)

@register.filter
def multiply(price, quantity):
    return price * quantity

@register.filter
def get_cart_total(cart, all_books):
    total = 0
    for book in all_books:
        quantity = cart.get(str(book.pk), 0)
        total += book.price * quantity
    return total
