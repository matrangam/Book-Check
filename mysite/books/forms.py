from django.forms import ModelForm
from django import forms
from books.models import Book, Topic
    
class NewBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('topic', 'title', 'author', 'quantity', 'description')
        
class NewTopicForm(ModelForm):
    class Meta:
        model = Topic        
        fields = ('tag',)