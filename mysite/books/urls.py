from django.conf.urls.defaults import *
from django.conf import settings
#
from books.models import Book, Topic
#
from os.path import join


urlpatterns = patterns('',
    
    url(r'^$', 'books.views.list', name="list"),
    
    url(r'^new$', 'books.views.add_book', name="add_book"),
    url(r'^(?P<book_id>\d+)/$', 'books.views.detail', name="detail"),
    
    url(r'^(?P<book_id>\d+)/checkout$', 'books.views.checkout', name="checkout"),
    url(r'^(?P<book_id>\d+)/returned$', 'books.views.returned', name="returned"),
    url(r'^(?P<book_id>\d+)/comments$', 'books.views.comments', name="comments"),

    url(r'^users$', 'books.views.users', name="users"),
    url(r'^new_user$', 'books.views.new_user', name="new_user"),

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'registration/login.html'}, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'registration/login.html'}, name="logout"),

    url(r'^assets/(?P<path>.*)$', 'django.views.static.serve', {'document_root': join(settings.PROJECT_ROOT, 'mysite/assets')}, name='assets'),

)