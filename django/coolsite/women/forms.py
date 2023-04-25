from django.core.exceptions import ValidationError
from django import forms
from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label= 'Caregoty is not choosen'
        
    class Meta:
       model = Women
       fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
       widget = {
           'title': forms.TextInput(attrs={'class': 'form-control'}),
           'content': forms.Textarea(attrs={'cols':60, 'rows':10}),
       }
       
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 150:
            raise ValidationError('Title is too long')
        return  title