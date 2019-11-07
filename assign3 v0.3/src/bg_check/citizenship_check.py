class Citizenship:
  def evaluate_criteria(self, social_security_number):
    if social_security_number % 10 >= 5:
      return (True, "")
    
    return (False, "Fail: not U.S. citizen")
