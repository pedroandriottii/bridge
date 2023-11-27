from .models import Demand, User
from .forms import SignupForm, AdminSignupForm, DemandForm
from django.contrib.auth import authenticate

def get_demands_by_status(status):
  demand = Demand.objects.filter(status=status)

  return demand

def get_project_info_by_user(user):
  demands = Demand.objects.filter(user=user)
  project = User.objects.filter(id=user)

  return {
    'demands': demands,
    'project': project
  }

class SearchDAO:
  @staticmethod
  def get_search_results(search_query):
    if search_query:
      return Demand.objects.filter(title__icontains=search_query)
    else:
      return Demand.objects.none() 

class AuthDAO:
  @staticmethod
  def create_user(form_data):
    form = SignupForm(form_data)
    if form.is_valid():
      return form.save()
    return None

  @staticmethod
  def authenticate_user(request, username, password):
    return authenticate(request, username=username, password=password)

  @staticmethod
  def create_user(form_data, role):
    form = AdminSignupForm(form_data)
    if form.is_valid():
      user = form.save(commit=False)
      user.role = role
      user.set_password(form.cleaned_data['password'])
      user.save()
      return user
    return None

class UserDAO:
  @staticmethod
  def create_demand(form_data, user):
    form = DemandForm(form_data)
    if form.is_valid():
      demand = form.save(commit=False)
      demand.user = user
      demand.save()
      return demand
    return None