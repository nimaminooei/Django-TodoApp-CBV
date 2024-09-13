from django import template

register = template.Library()

@register.filter(name='first_word')
def first_word(value):
    words = value.split()
    return words[0] if words else ''