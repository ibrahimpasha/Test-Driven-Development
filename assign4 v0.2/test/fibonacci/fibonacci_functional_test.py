import unittest
from src.fibonacci.fibonacci_functional import fibonacci_functional


class FibonacciFunctionalTest(unittest.TestCase):

  def test_functional_fibonacci_returns_1_for_position_0(self):
    self.assertEqual(1, fibonacci_functional(0))
    
  def test_functional_fibonacci_returns_1_for_position_1(self):
    self.assertEqual(1, fibonacci_functional(1))
  
  def test_functional_fibonacci_returns_5_for_position_4(self):
    self.assertEqual(5, fibonacci_functional(4))

  def test_functional_fibonacci_returns_21_for_position_7(self):
    self.assertEqual(21, fibonacci_functional(7))

  def test_functional_fibonacci_returns_None_for_position_less_than_zero(self):
    with self.assertRaises(ValueError):
      fibonacci_functional(-1)

  
if __name__ == '__main__':
  unittest.main()
