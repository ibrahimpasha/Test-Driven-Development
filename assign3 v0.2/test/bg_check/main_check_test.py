import unittest
from src.bg_check.main_check import check_single_criteria
from src.bg_check.criminal_history_check import CriminalHistory
from src.bg_check.credit_check import Credit


class Verification(unittest.TestCase):
  def test_check_single_criteria_with_criminal_history_fail(self):
    social_security_number = 455901755
    criminal_history = CriminalHistory()
    self.assertEqual(
      check_single_criteria(criminal_history, social_security_number),
      (False, "Fail: prior felony convictions"),
    )

  def test_check_single_criteria_with_criminal_history_pass(self):
    social_security_number = 455901752
    criminal_history = CriminalHistory()
    self.assertEqual(
      check_single_criteria(criminal_history, social_security_number),
      (True, "Pass"),
    )

  def test_check_single_criteria_with_credit_fail(self):
    social_security_number = 455901753
    credit = Credit()
    self.assertEqual(
      check_single_criteria(credit, social_security_number),
      (False, "Fail: credit score is less than 600"),
    )


if __name__ == "__main__":
    unittest.main()

