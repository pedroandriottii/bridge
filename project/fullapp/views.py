from .forms import SolicitationForm,SignupForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import Request
# Create your views here.

def solicitacao(request):
    if request.method == 'POST':
        form = SolicitationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('usuario/sucesso.html')
    else:
        form = SolicitationForm()

    return render(request, 'usuario/solicitacao.html', {'form': form})

def signup(request):
  if request.method == 'POST':
    print(request.POST)

    form = SignupForm(request.POST)

    if form.is_valid():
      user = form.save()

      print("criou")

      return redirect("signup")

  return render(request, 'auth/signup.html')

#@login_required
def add_manager(request):
  current_user = request.user

 #if current_user.role != 1:
    #return redirect("login")

  return render(request, 'management/add-manager.html')

#@login_required
def hom(request):
  current_user = request.user

  #if current_user.role != 1:
    #return redirect("login")

  return render(request, 'management/home.html')

def solicitacao (request):
  
  return render(request, 'usuario/solicitacao.html')