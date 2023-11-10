from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm, RequestForm
from .models import Project

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
  return redirect('common/index.html')

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

@login_required
def create_request(request, project_id):
  project = Project.objects.get(id=project_id)

  if request.method == 'POST':
    form = RequestForm(request.user, request.POST)
    if form.is_valid():
      request_obj = form.save(commit=False)
      request_obj.user = request.user
      request_obj.project = project
      request_obj.save()
      return render('usuario/solicitacao.html')
  else:
    form = RequestForm(request.user)
  return render(request, 'usuario/solicitacao.html', {'form': form, 'project': project})

def index(request):
  return render(request, 'commons/index.html')