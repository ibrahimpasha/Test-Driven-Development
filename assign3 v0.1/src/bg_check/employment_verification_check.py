from src.bg_check.base_criteria import BaseCriteria

class EmploymentVerification(BaseCriteria):
  def evaluate_criteria(self, social_security_number):
    if social_security_number % 3 == 0:
      return (True, 'Pass')
    else:    #Feedback: else is redundant after a return
      return (False, 'Fail: employment date reporting discrepancy')