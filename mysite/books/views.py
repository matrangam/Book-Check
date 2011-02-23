from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, Context, loader
# 
from books.models import Book, Topic 
from books.forms import *

def list(request):
    book = Book.objects.all()
    return render_to_response('list.html', {'book': book})
    
def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render_to_response('detail.html', {'book':book})
    
def add_book(request, book_id=None):
    book = get_object_or_404(Book, pk=book_id) if book_id else None 
    if request.method == 'POST':
        form = NewBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            return redirect('bookcheck:list')
    else:
        form = NewBookForm(instance=book)        
    return render_to_response('add_book.html', { 'form':form, 'book':book }, RequestContext(request))            

def checkout(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    quantity = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        form = NewBookForm(request.POST, request.FILES, instance=quantity)
        if form.is_valid():
            quantity = form.save(commit=False)
            quantity = quantity-1
            quantity.save()
        return redirect('bookcheck:detail', book_id=book_id)
    return render_to_response('checkout.html', { 'book':book, 'quantity':quantity }, RequestContext(request))    
