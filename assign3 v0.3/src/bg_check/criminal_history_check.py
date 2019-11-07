class CriminalHistory:
  def evaluate_criteria(self, social_security_number):
    if social_security_number % 2 == 0:
      return (True, '')
    
    return (False, 'Fail: prior felony convictions')
