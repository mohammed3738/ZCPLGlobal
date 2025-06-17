from django import template

register = template.Library()

@register.filter
def times(number):
    return range(int(number))

@register.filter
def subtract(value, arg):
    return int(value) - int(arg)
