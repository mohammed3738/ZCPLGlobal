from django import template

register = template.Library()

@register.filter
def times(number):
    """Returns a range for the given number"""
    try:
        return range(int(number))
    except:
        return range(0)

@register.filter
def subtract(value, arg):
    """Subtracts arg from value"""
    try:
        return int(value) - int(arg)
    except:
        return 0
