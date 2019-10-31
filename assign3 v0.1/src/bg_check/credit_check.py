from src.bg_check.base_criteria import BaseCriteria

class Credit(BaseCriteria):    #Feedback: let's reduce code here (just a simulation, no need for so much for that)
  def evaluate_criteria(self, social_security_number):
    if social_security_number % 10 >= 6:
      credit = 700
    else:
      credit = 300
    return self._credit_score_logic(credit)

  def _credit_score_logic(self, credit):
    if credit >= 600:
      return (True, 'Pass')
    else:
      return (False, 'Fail: credit score is less than 600')    
