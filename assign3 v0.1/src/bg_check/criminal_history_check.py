from src.bg_check.base_criteria import BaseCriteria

class CriminalHistory(BaseCriteria):
  def evaluate_criteria(self, social_security_number):
    if social_security_number % 2 == 0:
      return (True, 'Pass')
    else: #Feedback: no need for else after a return
      return (False, 'Fail: prior felony convictions')