from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User, Request, Project


class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('username', 'name', 'email', 'phone', 'password1', 'password2','region')

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['project', 'description']
    def __init__(self, user, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(userID=user.id)




   