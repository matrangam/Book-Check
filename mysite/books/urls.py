from django.conf.urls.defaults import *
from django.conf import settings
#
from books.models import Book, Topic

urlpatterns = patterns('',
    url(r'^$', 'books.views.list', name="list"),
    url(r'^new$', 'books.views.add_book', name="add_book"),
    url(r'^(?P<book_id>\d+)/$', 'books.views.detail', name="detail"),
    url(r'^(?P<book_id>\d+)/checkout$', 'books.views.checkout', name="checkout"),
    url(r'^(?P<book_id>\d+)/returned$', 'books.views.returned', name="returned"),
    
)