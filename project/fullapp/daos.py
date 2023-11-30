from .models import Demand
from .forms import SignupForm, AdminSignupForm, DemandForm

def get_demands_by_status(status):
  demand = Demand.objects.filter(status=status)

  return demand


class SearchDAO:
  @staticmethod
  def get_search_results(search_query):
    if search_query:
      return Demand.objects.filter(title__icontains=search_query)
    else:
      return Demand.objects.none() 

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

