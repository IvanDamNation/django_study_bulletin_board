from django import template
from django.db.models import Count

from board.models import Category

register = template.Library()


@register.inclusion_tag('board/list_categories.html')
def show_categories(arg1='Hello', arg2='world'):
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    return {'categories': categories, 'arg1': arg1, 'arg2': arg2}
