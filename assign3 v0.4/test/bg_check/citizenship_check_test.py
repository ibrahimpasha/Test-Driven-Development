import unittest
from src.bg_check.citizenship_check import Citizenship

class CitizenshipCheck(unittest.TestCase):

  def setUp(self):
    self.citizenship = Citizenship()

  def test_citizenship_check_True(self):
    social_security_number = 455901756
    self.assertEqual(
      self.citizenship.evaluate_criteria(social_security_number),
      (True, ''))

  def test_citizenship_check_False(self):
    social_security_number = 455901754
    self.assertEqual(
      self.citizenship.evaluate_criteria(social_security_number),
      (False, 'Fail: not U.S. citizen'))

if __name__ == '__main__':
  unittest.main()
