from django import template

register = template.Library()

@register.filter(name='get_option')
def get_option(question, option_num):
    """Get dynamic option text for questions"""
    try:
        return getattr(question, f'option{option_num}', '')
    except AttributeError:
        return ''


@register.filter
def subtract(value, arg):
    return value - arg

@register.filter
def divide(value, arg):
    return value / arg

@register.filter
def multiply(value, arg):
    return value * arg

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)        