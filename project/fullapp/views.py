from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignupForm, DemandForm, UserSignupForm, AdminSignupForm, EmbassadorSignupForm, DemandStatusForm, UpdateDemandForm
from .models import Demand, StatusEnum, RegionEnum, User
from .mediators import DemandMediator
from django.urls import reverse
from datetime import timedelta
from .mediators import SearchMediator, AuthMediator, ManagerMediator, UserMediator
#done
def search(request):
  mediator = SearchMediator()

  if request.method == 'POST':
    search_query = request.POST.get('search')
    return redirect(reverse('search') + '?q=' + search_query)
  else:
    search_query = request.GET.get('q')
    print(search_query)
    search_results = mediator.perform_search(search_query)
    return render(request, 'management/search.html', {'search_results': search_results})

def project_details(request, id):
    demand = Demand.objects.get(id=id)
    demands = Demand.objects.filter(status=StatusEnum.CONCLUDED, user =demand.user)


    print(demands)

    if demand.status == 'Buscando Doadores':
        form = UpdateDemandForm()

        if request.method == 'POST':
            form = UpdateDemandForm(request.POST, instance=demand)

            if form.is_valid():
                user = User.objects.get(username=form.cleaned_data['user'])
                demand = form.save(commit=False)
                demand.user = user
                demand.status = StatusEnum.DONORS_FOUND
                demand.save()

                return redirect('demands')
        else:
            form = UpdateDemandForm()

        ambassadors = User.objects.filter(role=2)

        return render(request, 'management/project/step-1.html', {
           'form': form,
           'demand': demand,
           'ambassadors': ambassadors,
           'demands': demands
        })
    elif demand.status == 'Doador Atribuido':
        return render(request, 'management/project/step-2.html', {
           'demand': demand,
           'demands': demands
        })
    else:
        return render(request, 'management/project/step-3.html', {
            'demand': demand,
            'demands': demands
        })

#done
def signup(request):
    mediator = AuthMediator()

    if request.method == 'POST':
        user = mediator.signup_user(request.POST)
        if user:
            login(request, user)
            messages.success(request, f'Conta criada para {user.name}!')
            return redirect("home")
        else:
            form = SignupForm(request.POST) 
    else:
        form = SignupForm()

    return render(request, 'auth/signup.html', {'form': form})

# def signup_user3(request):
#     if request.method == 'POST':
#         form = AdminSignupForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.role = 1
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             login(request, user)

#             return redirect('home')  
#     else:
#         form = AdminSignupForm()

#     return render(request, 'auth/signup_user3.html', {'form': form})
#done
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        mediator = AuthMediator()
        user = mediator.signin(request, username, password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login bem-sucedido.')
            return redirect('home')
        else:
            messages.error(request, 'Login inválido. Por favor, tente novamente.')

    return render(request, 'auth/login.html')
#done
@login_required
def add_manager(request):
    current_user = request.user

    if current_user.role != 1:
        return redirect("login")
  
    mediator = ManagerMediator()

    if request.method == 'POST':
        form = AdminSignupForm(request.POST)
        user = mediator.add_manager(request.POST)
        if user:
            return redirect('home')
        else:
            form = AdminSignupForm(request.POST)
    else:
        form = AdminSignupForm()

    return render(request, 'management/add-manager.html', {'form': form})
#done
@login_required
def add_ambassador(request):
  current_user = request.user
  arr = []

  if current_user.role != 1:
    return redirect("login")

  mediator = ManagerMediator()

  if request.method == 'POST':
    form = EmbassadorSignupForm(request.POST)
    user = mediator.add_ambassador(request.POST)
    if user:
      return redirect('home')
    else:
      form = EmbassadorSignupForm(request.POST) 
  else:
    for key, value in RegionEnum.__dict__.items():
      if value != 'fullapp.models' and value != 'None' and not str(value).startswith("<"):
        arr.append({
          'label': value,
          'value': key
        })

    arr.pop()
    arr.pop()
    arr.pop()
    arr = arr[1:]
    form = EmbassadorSignupForm()

  return render(request, 'management/add-ambassador.html', {'form': form, 'region_options': arr})

@login_required
def home(request):
  current_user = request.user

  if current_user.role == 1:
    return render(request, 'management/home.html')
  elif current_user.role == 2:
    return render(request, 'embassor/home.html')
  else:
    user_demands_concluded = Demand.objects.filter(user=request.user, status=StatusEnum.CONCLUDED)
    user_demands_in_analysis = Demand.objects.filter(user=request.user).exclude(status=StatusEnum.CONCLUDED)
    return render(request, "usuario/home.html", {
       'concluded_demands': user_demands_concluded,
       'in_analysis_demands': user_demands_in_analysis
    })

#done
@login_required
def demand_create(request):
    current_user = request.user
    if current_user.role == 3:
        mediator = UserMediator()

        if request.method == 'POST':
            form = DemandForm(request.POST)
            demand = mediator.create_demand(request.POST, request.user)
            if demand:
                return redirect('home')
            else:
                form = DemandForm(request.POST)  # Recria o formulário com os dados postados e erros
        else:
            form = DemandForm()

        return render(request, 'usuario/demand_create.html', {'form': form})
    else:
        return redirect('home')

@login_required
def demands_by_region(request):
    current_user = request.user

    if current_user.role == 1:
        region_demands = Demand.objects.exclude(status__in=[StatusEnum.REJECTED, StatusEnum.DEACTIVATED])
    elif current_user.role == 2:
        region_demands = Demand.objects.filter(region=current_user.region).exclude(status__in=[StatusEnum.REJECTED, StatusEnum.DEACTIVATED, StatusEnum.IN_ANALISYS])
    else:
        return redirect('home')

    return render(request, 'embassor/demands_by_region.html', {'region_demands': region_demands})


@login_required
def demands(request):
  current_user = request.user

  if current_user.role != 1:
    return redirect('home')
  
  demands = DemandMediator.get_demands()
  
  return render(request, 'management/demands.html', demands)

def demand_detail(request, demand_id):
    demand = get_object_or_404(Demand, id=demand_id)
    
    if request.method == 'POST':
        form = DemandStatusForm(request.POST, instance=demand)
        if form.is_valid():
            form.save()
            return redirect('demand_detail', demand_id=demand.id)
    else:
        form = DemandStatusForm(instance=demand)

    return render(request, 'embassor/demand_detail.html', {'demand': demand, 'form': form})

def triagem(request):
    current_user = request.user

    if current_user.role != 2:
        return redirect('home')

    demands = Demand.objects.filter(status=StatusEnum.IN_ANALISYS, region=current_user.region)

    return render(request, 'embassor/triagem.html', {'demands': demands})

def aprovar_triagem(request, demand_id):
    current_user = request.user

    if current_user.role != 2:
        return redirect('home')
    try:
        demand = Demand.objects.get(id=demand_id)

        if demand.status == StatusEnum.IN_ANALISYS and demand.region == current_user.region:
            demand.status = StatusEnum.APPROVED
            demand.save()

            messages.success(request, 'Triagem aprovada com sucesso!')
        else:
            messages.error(request, 'Não é possível aprovar a triagem para esta demanda.')

    except Demand.DoesNotExist:
        messages.error(request, 'Demanda não encontrada.')

    return redirect('triagem')

def rejeitar_triagem(request, demand_id):
  current_user = request.user

  if current_user.role != 2:
      return redirect('home')

  try:
      demand = Demand.objects.get(id=demand_id)

      if demand.status == StatusEnum.IN_ANALISYS and demand.region == current_user.region:
          demand.status = StatusEnum.REJECTED
          demand.save()

          messages.success(request, 'Triagem rejeitada com sucesso!')
      else:
          messages.error(request, 'Não é possível rejeitar a triagem para esta demanda.')

  except Demand.DoesNotExist:
      messages.error(request, 'Demanda não encontrada.')

  return redirect('triagem')
