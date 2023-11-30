from .daos import SearchDAO, get_demands_by_status, UserDAO
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
    looking_for_donors = get_demands_by_status(status=StatusEnum.LOOKING_FOR_DONORS)
    donors_found = get_demands_by_status(status=StatusEnum.DONORS_FOUND)
    concluded = get_demands_by_status(status=StatusEnum.CONCLUDED)

    return {
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

    def add_manager(self, form_data):
      return self.auth_dao.create_user(form_data, role=1)

    def add_ambassador(self, form_data):
        return self.auth_dao.create_user(form_data, role=2)