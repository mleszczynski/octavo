# -*- coding: utf-8 -*-

from django.views.defaults import page_not_found, server_error
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404

from octavo.main import models as octavo_models
from octavo.main import forms as octavo_forms


def index(request):
    ctx_data = {
    }
    return render_to_response('index.html', ctx_data, context_instance=RequestContext(request))

def books(request):
    books = octavo_models.Book.objects.all()
    ctx_data = {
        'books': books,
    }
    return render_to_response('books.html', ctx_data, context_instance=RequestContext(request))


def book(request, book_id):
    try:
        book = octavo_models.Book.objects.get(id=book_id)
        ctx_data = {
            'book': book,
        }
        return render_to_response('book.html', ctx_data, context_instance=RequestContext(request))
    except octavo_models.Book.DoesNotExist:
        raise Http404
    

def book_add(request):
    if request.method == "POST":
        form = octavo_forms.BookAddForm(request.POST)
        if form.is_valid():
            form.save()
            # Do something.
    else:
        form = octavo_forms.BookAddForm()
    
    ctx_data = {
        'form': form,
    }    
    return render_to_response("book_add.html", ctx_data, context_instance=RequestContext(request))


def handler404(request):
    return page_not_found(request, "404.html")


def handler500(request):
    return server_error(request, '500.html')