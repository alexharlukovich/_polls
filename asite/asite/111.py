# from django import template
# s = template.Template('Меня зовут {{ name }}.')
# v = template.Context({'name': 'Адриан'})
# print (s.render(v))

from django.template import Context, Template
t = Template('Меня зовут {{ name }}.')
c = Context({'name':'Стефан'})
t.render(c)
u’Меня зовут Стефан.’