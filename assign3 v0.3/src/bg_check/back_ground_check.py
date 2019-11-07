from src.bg_check.credit_check import Credit
from src.bg_check.citizenship_check import Citizenship
from src.bg_check.criminal_history_check import CriminalHistory
from src.bg_check.employment_verification_check import EmploymentVerification


class BackgroundCheck:
  def __init__(self):
    self.mapping = {'credit_check': Credit(),
                    'citizen_check': Citizenship(),
                    'criminal_check': CriminalHistory(),
                    'employment_check': EmploymentVerification()
                    }
  
  def evaluate_criteria(self, criteria_list=[], candidate_SSN=None):
    evaluation_results = {criteria: self.mapping[criteria].evaluate_criteria(candidate_SSN) for criteria in criteria_list}
    return True if all(list(map(lambda x: x[0], evaluation_results.values()))) else list(map(lambda x: x[1], evaluation_results.values()))
