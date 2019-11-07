import unittest
from src.bg_check.employment_verification_check import EmploymentVerification

class EmploymentVerificationCheck(unittest.TestCase):
  def setUp(self):
    self.employment = EmploymentVerification()

  def test_employment_verification_check_True(self):
    social_security_number = 455901756
    self.assertEqual(
      self.employment.evaluate_criteria(social_security_number), (True, "")
    )

  def test_employment_verification_check_False(self):
    social_security_number = 455901754
    self.assertEqual(
      self.employment.evaluate_criteria(social_security_number),
      (False, "Fail: employment date reporting discrepancy"),
    )


if __name__ == "__main__":
    unittest.main()
