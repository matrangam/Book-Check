from django.conf.urls.defaults import *
from django.conf import settings

from books.models import Book, Topic

urlpatterns = patterns('',
    url(r'^$', 'books.views.book_detail', name="book_list"),
)