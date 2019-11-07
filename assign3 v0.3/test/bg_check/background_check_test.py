import unittest
from src.bg_check.back_ground_check import BackgroundCheck

class BackgroundCheckTest(unittest.TestCase):

  def setUp(self):
    self.bgcheck = BackgroundCheck()
    
  def test_canary(self):
    self.assertTrue(True)
  
  def test_background_check_with_multiple_criteria_no_failure(self):
    candidate_ssn = 455901756
    self.assertEqual(True, self.bgcheck.evaluate_criteria(\
      criteria_list=['credit_check', 'citizen_check', 'criminal_check', 'employment_check'], \
      candidate_SSN=candidate_ssn))
    
  def test_background_check_with_multiple_criteria_one_failure(self):
    candidate_ssn = 454901756
    expected_result = ['', '', '', 'Fail: employment date reporting discrepancy']
    self.assertEqual(expected_result, self.bgcheck.evaluate_criteria(\
      criteria_list=['credit_check', 'citizen_check', 'criminal_check', 'employment_check'], \
      candidate_SSN=candidate_ssn))
    
  def test_background_check_with_multiple_criteria_two_failure(self):
    candidate_ssn = 454901754
    expected_result = ['Fail: credit score is less than 600', 'Fail: not U.S. citizen', '', '']
    self.assertEqual(expected_result, self.bgcheck.evaluate_criteria(\
      criteria_list=['credit_check', 'citizen_check', 'criminal_check', 'employment_check'], \
      candidate_SSN=candidate_ssn))
    
  def test_background_check_with_multiple_criteria_three_failure(self):
    candidate_ssn = 455901753
    expected_result = ['Fail: credit score is less than 600', 'Fail: not U.S. citizen', 'Fail: prior felony convictions', '']
    self.assertEqual(expected_result, self.bgcheck.evaluate_criteria(\
      criteria_list=['credit_check', 'citizen_check', 'criminal_check', 'employment_check'], \
      candidate_SSN=candidate_ssn))
    
if __name__ == '__main__':
  unittest.main()