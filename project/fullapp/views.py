from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm, DemandForm, UserSignupForm, AdminSignupForm, EmbassadorSignupForm
from .models import Demand, StatusEnum

def signup(request):
  if request.method == 'POST':
    form = SignupForm(request.POST)

    if form.is_valid():
      user = form.save()
      login(request, user)
      messages.success(request, f'Conta criada para {user.name}!')
      return redirect("sign-in")
  else:
    form = SignupForm()
  return render(request, 'auth/signup.html', {'form': form})

def signup_user2(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 2
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)

            return redirect('home')  
    else:
        form = UserSignupForm()

    return render(request, 'auth/signup_user2.html', {'form': form})

def signup_user3(request):
    if request.method == 'POST':
        form = AdminSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 1
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)

            return redirect('home')  
    else:
        form = AdminSignupForm()

    return render(request, 'auth/signup_user3.html', {'form': form})

def signin(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
      if user.role in [2, 3]:
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
  
  if request.method == 'POST':
    form = AdminSignupForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.role = 1
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('home')  
  else:
    form = AdminSignupForm()

  return render(request, 'management/add-manager.html', { 'form': form })

@login_required
def add_embassador(request):
  current_user = request.user

  if current_user.role != 1:
    return redirect("login")
  
  if request.method == 'POST':
    form = EmbassadorSignupForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.role = 2
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect('home')  
  else:
    form = EmbassadorSignupForm()

  return render(request, 'management/add-embassador.html', { 'form': form })

@login_required
def home(request):
  current_user = request.user

  if current_user.role == 1:
    return render(request, 'management/home.html')
  elif current_user.role == 2:
    return render(request, 'embassor/home.html')
  else:
    user_demands_concluded = Demand.objects.filter(user=request.user, status=StatusEnum.CONCLUDED)
    user_demands_in_analysis = Demand.objects.filter(user=request.user, status=StatusEnum.LOOKING_FOR_DONORS)

    return render(request, "usuario/home.html", {
       'concluded_demands': user_demands_concluded,
       'in_analysis_demands': user_demands_in_analysis
    })

def index(request):
  return render(request, 'commons/index.html')

@login_required
def demand_create(request):
  current_user = request.user
  if current_user.role == 3:
    if request.method == 'POST':
        form = DemandForm(request.POST)
        if form.is_valid():
            demand = form.save(commit=False)
            demand.user = request.user  
            demand.save()
            return redirect('home')
    else:
        form = DemandForm()

    return render(request, 'usuario/demand_create.html', {'form': form})
  else:
    return redirect('home')

@login_required
def my_demands(request):
  current_user = request.user
  if current_user.role == 3:
    if request.user.is_authenticated:
        user_demands = Demand.objects.filter(user=request.user)
        return render(request, 'usuario/my_demands.html', {'user_demands': user_demands})
    else:
        return render(request, 'usuario/my_demands.html', {'user_demands': None})
  else:
    return redirect('home')

@login_required
def demands_by_region(request):
    current_user = request.user

    if current_user.role == 1:
        region_demands = Demand.objects.all()
    elif current_user.role == 2:
        region_demands = Demand.objects.filter(region=current_user.region)
    else:
        return redirect('home')

    return render(request, 'embassor/demands_by_region.html', {'region_demands': region_demands})


@login_required
def demands(request):
  current_user = request.user

  if current_user.role != 1:
    return redirect('home')
  
  return render(request, 'management/demands.html')