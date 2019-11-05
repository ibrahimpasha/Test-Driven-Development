import unittest
from src.bg_check.criminal_history_check import CriminalHistory

class CriminalHistoryCheck(unittest.TestCase):
  def setUp(self):
    self.criminal_history = CriminalHistory()

  def test_criminal_history_check_True(self):
    social_security_number = 455901868
    self.assertEqual(
      self.criminal_history.evaluate_criteria(social_security_number),
      (True, ''))

  def test_criminal_history_check_False(self):
    social_security_number = 455901867
    self.assertEqual(
      self.criminal_history.evaluate_criteria(social_security_number),
      (False, 'Fail: prior felony convictions'))


if __name__ == '__main__':
  unittest.main()
