from django import template

register = template.Library()

@register.filter
def sub(value, arg):
    return int(value) - int(arg)

@register.filter
def evaluate(value, arg):
    L = len(value)
    V = 0
    if L%2 == 0:
        V =  L/int(arg)
    else:
        V = L//int(arg) + 1
        
    return V