from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, Context, loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# 
from books.models import *
from books.forms import *

def list(request):
    book = Book.objects.all()
    return render_to_response('list.html', {'book': book})


def users(request, user_id=None):
    users = User.objects.all()
    return render_to_response('users.html', {'users':users})


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render_to_response('detail.html', {'book':book, 'user': request.user})


def user_detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render_to_response('user_detail.html', {'user':user})    


def add_book(request, book_id=None):
    book = get_object_or_404(Book, pk=book_id) if book_id else None 
    if request.method == 'POST':
        form = NewBookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('bookcheck:list')
    else:
        form = NewBookForm(instance=book)        
    return render_to_response('add_book.html', { 'form':form, 'book':book }, RequestContext(request))


def login(request, user_id=None):
    user = get_object_or_404(User, pk=user_id) if user_id else None
    return redirect('bookcheck:login', {'user':user}, RequestContext(request.user))
                


def new_user(request, user_id=None):
    user = get_object_or_404(User, pk=user_id) if user_id else None
    if request.method == 'POST':
        form = NewUserForm(request.POST, request.FILES, instance=user)    
        if form.is_valid():
            user = form.save()
            return redirect('bookcheck:users')
    else:
        form = NewUserForm(instance=user)
    return render_to_response('new_user.html', { 'form':form, 'user':user }, RequestContext(request))                 

def checkout(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    user = (book.users)
    if request.method == 'POST' and book.quantity > 0:
        book.quantity = book.quantity - 1
        book.save()
        book.users.add(request.user)
        return redirect('bookcheck:detail', book_id=book_id)
    
    return render_to_response('checkout.html', { 'book':book, 'user':request.user }, RequestContext(request))    

def returned(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method =='POST':
        book.quantity = book.quantity + 1
        book.save()
        book.users.remove(request.user)
        return redirect('bookcheck:detail', book_id)
        
    return render_to_response('returned.html', { 'book':book }, RequestContext(request)) 
