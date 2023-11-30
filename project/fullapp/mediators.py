from .daos import SearchDAO, get_demands_by_status, get_demands_by_date, UserDAO,  AuthDAO
from .models import StatusEnum

class SearchMediator:
  def __init__(self):
    self.dao = SearchDAO()

  def perform_search(self, search_query):
    if search_query:
      return self.dao.get_search_results(search_query)
    else:
        return []

class DemandMediator:
  def get_demands():
    oldest_demands = get_demands_by_date("oldest")
    looking_for_donors = get_demands_by_status(status=StatusEnum.LOOKING_FOR_DONORS)
    donors_found = get_demands_by_status(status=StatusEnum.DONORS_FOUND)
    concluded = get_demands_by_status(status=StatusEnum.CONCLUDED)

    print(oldest_demands)

    return {
      'oldest_demands': oldest_demands,
      'looking_for_donors': looking_for_donors,
      'donors_found': donors_found,
      'concluded': concluded
    }
  
  def get_project_details():
    looking_for_donors = get_demands_by_status(status=StatusEnum.LOOKING_FOR_DONORS)

class UserMediator:
  def __init__(self):
    self.user_dao = UserDAO()

  def create_demand(self, form_data, user):
    return self.user_dao.create_demand(form_data, user)

class ManagerMediator:
    def __init__(self):
      self.auth_dao = AuthDAO()

    def add_manager(self, form_data):
      return self.auth_dao.create_user(form_data, role=1)

    def add_ambassador(self, form_data):
        return self.auth_dao.create_user(form_data, role=2)
    
    def home():
      most_recent_demands = get_demands_by_date("latest")
      oldest_demands = get_demands_by_date("oldest")[:5]

      print(most_recent_demands)
      
      return {
        'most_recent_demands': most_recent_demands,
        'oldest_demands': oldest_demands
      }
