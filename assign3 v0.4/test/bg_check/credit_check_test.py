import unittest
from src.bg_check.credit_check import Credit

class CreditCheck(unittest.TestCase):
  def setUp(self):
    self.credit = Credit()

  def test_evaluate_criteria_returns_True(self):
    social_security_number = 455901867
    self.assertEqual(self.credit.evaluate_criteria(social_security_number),
      (True, ''))

  def test_evaluate_criteria_logic_returns_False(self):
    social_security_number = 455901862
    self.assertEqual(self.credit.evaluate_criteria(social_security_number),
      (False, 'Fail: credit score is less than 600'))

if __name__ == '__main__':
  unittest.main()
