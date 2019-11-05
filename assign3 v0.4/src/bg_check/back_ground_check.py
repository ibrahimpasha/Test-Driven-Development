from src.bg_check.credit_check import Credit
from src.bg_check.citizenship_check import Citizenship
from src.bg_check.criminal_history_check import CriminalHistory
from src.bg_check.employment_verification_check import EmploymentVerification


def evaluate_selected_criteria(criteria_list = [], candidate_SSN = None):
  booleans, reasons = zip(
    *map(lambda criteria: criteria.evaluate_criteria(candidate_SSN), criteria_list)
  )

  return (True, "") if all(booleans) else (False, ", ".join(filter(None, reasons)))
