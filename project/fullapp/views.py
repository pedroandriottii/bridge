from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm, DemandForm
from .models import Demand
from django.http import HttpResponse

def signup(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)

    if form.is_valid():
      user = form.save()
      login(request, user)
      messages.success(request, f'Conta criada para {user.name}!')
      return redirect("signin")
  else:
    form = SignupForm()
  return render(request, 'auth/signup.html', {'form': form})

def signin(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request, 'Login bem-sucedido.')
      return redirect('home')  
    else:
      messages.error(request, 'Login inválido. Por favor, tente novamente.')
  return render(request, 'auth/login.html')

def logout(request):
  logout(request)
  messages.success(request, 'Logout bem-sucedido.')
  return redirect('signin')

@login_required
def add_manager(request):
  current_user = request.user

  if current_user.role != 1:
    return redirect("login")

  return render(request, 'management/add-manager.html')

@login_required
def hom(request):
  current_user = request.user

  if current_user.role == 1:
    return render(request, 'management/home.html')
  elif current_user.role == 2:
    return render(request, 'embassor/home.html')
  else:
    return render(request, "usuario/home.html")

def index(request):
  return render(request, 'commons/index.html')

def demand_create(request):
  if request.method == 'POST':
      form = DemandForm(request.POST)
      if form.is_valid():
          demand = form.save(commit=False)
          demand.user = request.user  # Associar a demanda ao usuário atual
          demand.save()
          return redirect('demand-list')  # Substitua pelo nome da sua view de lista de demandas
  else:
      form = DemandForm()

  return render(request, 'usuario/demand_create.html', {'form': form})

def my_demands(request):
    if request.user.is_authenticated:
        user_demands = Demand.objects.filter(user=request.user)
        return render(request, 'usuario/my_demands.html', {'user_demands': user_demands})
    else:
        return render(request, 'usuario/my_demands.html', {'user_demands': None})