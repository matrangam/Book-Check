from django.forms import ModelForm
from django import forms
#
from books.models import *
    
class NewBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('topic', 'title', 'author', 'quantity', 'description', 'comments')
        
class NewTopicForm(ModelForm):
    class Meta:
        model = Topic        
        fields = ('tag',)
        
class NewUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        
class PartialBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('comments', )
        
