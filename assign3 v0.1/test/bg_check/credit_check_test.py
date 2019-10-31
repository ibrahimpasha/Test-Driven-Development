import unittest
from src.bg_check.credit_check import Credit


class CreditCheck(unittest.TestCase):
  def setUp(self):
    self.credit = Credit()

  def test_private_credit_score_logic_returns_True_for_credit_more_than_600(self):
    self.assertEqual(self.credit._credit_score_logic(780), (True, 'Pass'))

  def test_private_credit_score_logic_returns_False_for_credit_less_than_600(self):
    self.assertEqual(self.credit._credit_score_logic(500), \
      (False, 'Fail: credit score is less than 600'))

  def test_evaluate_criteria_returns_True(self):
    social_security_number = 455901867
    self.assertEqual(self.credit.evaluate_criteria(social_security_number), (True, 'Pass'))

  def test_evaluate_criteria_logic_returns_False(self):
    social_security_number = 455901862
    self.assertEqual(self.credit.evaluate_criteria(social_security_number), \
      (False, 'Fail: credit score is less than 600'))
if __name__ == '__main__':
  unittest.main()
