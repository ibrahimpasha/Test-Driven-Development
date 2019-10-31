class Credit:
  def evaluate_criteria(self, social_security_number):
    if social_security_number % 10 >= 6:
      return (True, 'Pass')
    return (False, 'Fail: credit score is less than 600')