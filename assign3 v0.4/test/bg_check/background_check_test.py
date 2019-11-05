import unittest
from src.bg_check.back_ground_check import evaluate_selected_criteria
from src.bg_check.credit_check import Credit
from src.bg_check.citizenship_check import Citizenship
from src.bg_check.criminal_history_check import CriminalHistory
from src.bg_check.employment_verification_check import EmploymentVerification

class BackgroundCheckTest(unittest.TestCase):
    
  def test_canary(self):
    self.assertTrue(True)

  def test_background_check_with_multiple_criteria_no_failure(self):
    candidate_ssn = 455901756
    self.assertEqual((True, ''), evaluate_selected_criteria(
      criteria_list = [Credit(), Citizenship(), CriminalHistory(), 
                       EmploymentVerification()],
      candidate_SSN = candidate_ssn))

  def test_background_check_with_multiple_criteria_one_failure(self):
    candidate_ssn = 454901756
    expected_result = (False, 'Fail: employment date reporting discrepancy')
    self.assertEqual(expected_result, evaluate_selected_criteria(
      criteria_list = [Credit(), Citizenship(), CriminalHistory(), 
                       EmploymentVerification()],
      candidate_SSN = candidate_ssn))

  def test_background_check_with_multiple_criteria_two_failure(self):
    candidate_ssn = 454901754
    expected_result = (False, 'Fail: credit score is less than 600, Fail: not U.S. citizen')
    self.assertEqual(expected_result, evaluate_selected_criteria(
      criteria_list = [Credit(), Citizenship(), CriminalHistory(), 
                       EmploymentVerification()],
      candidate_SSN = candidate_ssn))

  def test_background_check_with_multiple_criteria_three_failure(self):
    candidate_ssn = 455901753
    expected_result = (False, 'Fail: credit score is less than 600, '
                       'Fail: not U.S. citizen, Fail: prior felony convictions')
    self.assertEqual(expected_result, evaluate_selected_criteria(
      criteria_list = [Credit(), Citizenship(), CriminalHistory(), 
                       EmploymentVerification()],
      candidate_SSN = candidate_ssn))

if __name__ == '__main__':
  unittest.main()
