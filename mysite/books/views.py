from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
#
from books.models import Book, Topic 

def book_detail(request):
    book = Book.objects.all()
    return render_to_response('all_books.html', {'book': book})