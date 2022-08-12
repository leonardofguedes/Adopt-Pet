from django import template
from dogncat.models import Animal

register = template.Library()


@register.simple_tag
def total_animals():
    return Animal.objects.count()