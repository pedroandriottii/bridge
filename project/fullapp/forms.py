from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User, Request, Request


class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'password1', 'password2']

class SolicitationForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name', 'phone', 'project', 'region','title', 'description' ]



   