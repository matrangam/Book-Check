from django.conf.urls.defaults import *
from django.conf import settings

from books.models import Book, Topic

urlpatterns = patterns('',
    url(r'^$', 'books.views.book_list', name="book_list"),
    url(r'^new$', 'books.views.add_book', name="add_book"),
    url(r'^(?P<book_id>\d+)/$', 'books.views.book_detail', name="book_detail"),
    
)