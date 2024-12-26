from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
def hellopage(request):
    template = loader.get_template('page.html')
    return HttpResponse(template.render())

