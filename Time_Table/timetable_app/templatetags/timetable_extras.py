from django import template

register = template.Library()

@register.filter
def to(value, arg):
    """Usage: {% for i in 1|to:9 %} ... {% endfor %} will loop 1 to 8"""
    return range(value, int(arg))

