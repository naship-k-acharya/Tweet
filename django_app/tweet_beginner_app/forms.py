from django import forms
from .models import Tweet,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TweetForm(forms.ModelForm):
    
    class Meta:
        model = Tweet
        fields = ['text','photo']

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
  password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')

# from for comment
class CommentForm(forms.ModelForm):
   class Meta:
      model = Comment
      fields = ('text',)  # fields is a list of field names
      