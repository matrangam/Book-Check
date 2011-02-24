from django.forms import ModelForm
from django import forms
#
from books.models import *
    
class NewBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('topic', 'title', 'author', 'quantity', 'description', 'user')
        
class NewTopicForm(ModelForm):
    class Meta:
        model = Topic        
        fields = ('tag',)
        
class NewUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('user_name', 'email', 'books')