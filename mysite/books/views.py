from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, Context, loader
# 
from books.models import Book, Topic 
from books.forms import *

def book_list(request):
    book = Book.objects.all()
    form = BookForm()
    return render_to_response('all_books.html', {'book': book})
    
def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render_to_response('book_detail.html', {'book':book})
    
def add_book(request, book_id=None):
    #book = get_object_or_404(Book, pk=book_id) 
    form = NewBookForm()
    return render_to_response('add_book.html', { 'form':form })            
