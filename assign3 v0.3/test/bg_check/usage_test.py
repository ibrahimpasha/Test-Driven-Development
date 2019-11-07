# import unittest
# import src.bg_check as bg
#
# #Feedback: let's name files based on the class they contain
#
# #Feedback: we can remove this entire file
#
# class EmploymentVerificationCheck(unittest.TestCase):
#
#   def test_choose_all_predefined_criteria_all_true(self):
#     social_security_number = 455901756
#
#     citizenship = bg.citizenship_check.Citizenship()
#     credit = bg.credit_check.Credit()
#     criminal_history = bg.criminal_history_check.CriminalHistory()
#     employment = bg.employment_verification_check.EmploymentVerification()
#
#     self.assertEqual(
#       [citizenship.evaluate_criteria(social_security_number),
#       credit.evaluate_criteria(social_security_number),
#       criminal_history.evaluate_criteria(social_security_number),
#       employment.evaluate_criteria(social_security_number)],
#       [(True, ""),
#       (True, ""),
#       (True, ""),
#       (True, "")]
#     )
#
#   def test_choose_all_predefined_criteria_most_false(self):
#     social_security_number = 455901753
#
#     citizenship = bg.citizenship_check.Citizenship()
#     credit = bg.credit_check.Credit()
#     criminal_history = bg.criminal_history_check.CriminalHistory()
#     employment = bg.employment_verification_check.EmploymentVerification()
#
#     self.assertEqual(
#       [citizenship.evaluate_criteria(social_security_number),
#       credit.evaluate_criteria(social_security_number),
#       criminal_history.evaluate_criteria(social_security_number),
#       employment.evaluate_criteria(social_security_number)],
#       [(False, "Fail: not U.S. citizen"),
#       (False, "Fail: credit score is less than 600"),
#       (False, "Fail: prior felony convictions"),
#       (True, "")]
#     )
#
#   def test_add_new_criteria(self):
#     social_security_number = 455901753
#
#     citizenship = bg.citizenship_check.Citizenship()
#     credit = bg.credit_check.Credit()
#
#     class NewCriteria_ProfessionalSocialMedia:
#       def evaluate_criteria(self, social_security_number):
#         if social_security_number % 10 >= 3:
#           return (True, '')
#
#         return (False, 'Fail: Social media presence is unprofessional')
#
#     professional_social_media = NewCriteria_ProfessionalSocialMedia()
#
#     self.assertEqual(
#       [citizenship.evaluate_criteria(social_security_number),
#       credit.evaluate_criteria(social_security_number),
#       professional_social_media.evaluate_criteria(social_security_number)],
#       [(False, "Fail: not U.S. citizen"),
#       (False, "Fail: credit score is less than 600"),
#       (True, "")]
#     )
#
#
# if __name__ == "__main__":
#     unittest.main()
