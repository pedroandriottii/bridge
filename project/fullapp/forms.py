from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User, Demand


class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('username', 'name', 'email', 'phone', 'password1', 'password2','region', 'project', 'objective')

class DemandForm(forms.ModelForm):
    class Meta:
        model = Demand
        fields = ['title', 'description', 'region']

class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'phone', 'email', 'region']

class AdminSignupForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password', 'name', 'phone', 'email']
   