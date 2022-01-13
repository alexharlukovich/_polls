# from django.shortcuts import render
# from django.http import Http404, HttpResponse
# from django.template import Template, Context
# import datetime

from django.template import Template, Context
from django.http import HttpResponse
# import datetime

# def hello(request):
#     return HttpResponse('Привет сайт!')

# def current_datetime(request):
#     now = datetime.datetime.now()
#     t = Template("<html><body>Сейчас ты ебаное быдло FUCK YO UP! {{ current_date }}.</body></html>")
#     html = t.render(Context({'current_date': now}))
#     return HttpResponse(html)
