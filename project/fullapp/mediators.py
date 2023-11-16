from .daos import get_demands_by_status
from .models import StatusEnum

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