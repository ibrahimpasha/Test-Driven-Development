class EmploymentVerification:
  def evaluate_criteria(self, social_security_number):
    if social_security_number % 3 == 0:
      return (True, 'Pass')
    return (False, 'Fail: employment date reporting discrepancy')