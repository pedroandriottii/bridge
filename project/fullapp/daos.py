# from .models import Project
from .models import Demand

# def get_projects():
#   products = Project.objects.all()

#   return products

# def get_project(pk):
#   project = Project.objects.get(pk=pk)

#   return project

def get_demands_by_status(status):
  demand = Demand.objects.filter(status=status)

  return demand