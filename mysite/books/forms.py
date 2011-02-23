from django.forms import ModelForm
from django import forms
from books.models import Book, Topic

class TopicForm(forms.Form):
    tag = forms.CharField(max_length=25)

class BookForm(forms.Form):
    topic = forms.ModelMultipleChoiceField(queryset=Topic.objects.all())
    title = forms.CharField(max_length=500)
    author = forms.CharField(max_length=100)
    quantity = forms.IntegerField()
    description = forms.CharField(max_length=500)  
    
class NewBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('topic', 'title', 'author', 'quantity', 'description')
        
class NewTopicForm(ModelForm):
    class Meta:
        model = Topic        
        fields = ('tag',)
        
        