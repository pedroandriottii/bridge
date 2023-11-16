from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import User, Demand, StatusEnum, RegionEnum, get_choices

INPUT_CLASSES = 'w-full mt-2 px-4 py-2 rounded-xl bg-[#FDFDFD] border border-[#D9D9D9]'

class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ('username', 'name', 'email', 'phone', 'password1', 'password2','region', 'project', 'objective')

class DemandForm(forms.ModelForm):
    class Meta:
        model = Demand
        fields = ['title', 'description', 'region']
        labels = {
          'title': 'Título',
          'description': 'Descrição',
          'region': 'Região',
        }

        widgets = {
          'title': forms.TextInput(attrs={
            'class': INPUT_CLASSES
          }),
          'description': forms.Textarea(attrs={
            'class': INPUT_CLASSES + " resize-none h-[150px]"
          }),
          'region': forms.Select(attrs={'class': INPUT_CLASSES }),
        }

class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'phone', 'email', 'region']

class AdminSignupForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password', 'name', 'phone', 'email']
    labels = {
      'username': 'Nome de usuário',
      'password': 'Senha',
      'name': 'Nome',
      'phone': 'Telefone',
      'email': 'E-mail',
    }

    widgets = {
      'username': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'password': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'name': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'phone': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'email': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      })
    }

class EmbassadorSignupForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'password', 'name', 'phone', 'email']
    labels = {
      'username': 'Nome de usuário',
      'password': 'Senha',
      'name': 'Nome',
      'phone': 'Telefone',
      'email': 'E-mail',
    }

    widgets = {
      'username': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'password': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'name': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'phone': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      }),
      'email': forms.TextInput(attrs={
        'class': INPUT_CLASSES
      })
    }

class DemandStatusForm(forms.ModelForm):
    status = forms.ChoiceField(choices=get_choices(StatusEnum))

    class Meta:
        model = Demand
        fields = ['status']