from django import template
register = template.Library()

@register.simple_tag
def calcSp(price,discount):
    if discount is None:
        return price
    sp=((100-discount)/100)*price
    return sp