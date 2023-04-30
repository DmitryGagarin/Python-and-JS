from django.core.exceptions import ValidationError
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
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
    
class RegisterUserForm(UserCreationForm):
    username = forms.CharField(help_text='')
    password1 = forms.CharField(help_text='')
    password2 = forms.CharField(help_text='')
    email = forms.EmailField(help_text='')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
        
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(help_text='')
    password = forms.CharField(help_text='')
    
    