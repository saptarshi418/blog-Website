from django import forms
from .models import WriteBlog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BlogForm(forms.ModelForm):
    class Meta:
        model = WriteBlog
        fields = ['title','categories','coverImg','description']
        

class UserRegistrationForm(UserCreationForm):
    
    email = forms.EmailField()
    class Meta:
        model=User
        fields = ('username','email','password1','password2')


class UserLoginForm(forms.Form):
   username = forms.CharField(label="username", max_length=254, required=True )
   password = forms.CharField(label="password",widget = forms.PasswordInput(), required=True)

   
