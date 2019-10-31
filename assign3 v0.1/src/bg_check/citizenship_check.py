from src.bg_check.base_criteria import BaseCriteria

class Citizenship(BaseCriteria):
  def evaluate_criteria(self, social_security_number):
    if social_security_number % 10 >= 5:
      return (True, "Pass")
    else:
      return (False, "Fail: not U.S. citizen")
