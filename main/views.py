# -*- coding: utf-8 -*-

from django.views.defaults import page_not_found, server_error
from django.shortcuts import render_to_response
from django.template import RequestContext

from octavo.main import models as octavo_models
from octavo.main import forms as octavo_forms


def index(request):
    ctx_data = {
    }
    return render_to_response('index.html', ctx_data, context_instance=RequestContext(request))

def add_book(request):
    if request.method == "POST":
        form = octavo_forms.BookForm(request.POST)
        if form.is_valid():
            form.save()
            # Do something.
    else:
        form = octavo_forms.BookForm()
    
    ctx_data = {
        'form': form,
    }    
    return render_to_response("book.html", ctx_data, context_instance=RequestContext(request))


def handler404(request):
    return page_not_found(request, "404.html")

def handler500(request):
    return server_error(request, '500.html')