from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from .utils import mobileBrowser


def index(request):
    """ Render the index page """
    if mobileBrowser(request):
        t = loader.get_template('m_index.html')
    else:
        t = loader.get_template('index.html')
    
    context = {
        'site_name': 'Youtube Tutorial'
    } # normally your page data goes here.

    return HttpResponse(t.render(context))
