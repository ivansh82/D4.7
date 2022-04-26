from django import template

register = template.Library()


@register.filter()
def censor(value):
   text_censor = ['редиска', 'дурак']
   for i in text_censor:
      if i in value:
         value = value.replace(i, '*')
   return value