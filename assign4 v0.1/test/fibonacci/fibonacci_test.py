import unittest
from src.fibonacci.fibonacci import fibonacci_imperative

class FibonacciTest(unittest.TestCase):
  
  
  def test_canary(self):
    self.assertTrue(True)
  
  def test_imperative_fibonacci_returns_0_for_n_value_0(self):
    self.assertEqual(0, fibonacci_imperative(0))
    
  def test_imperative_fibonacci_returns_1_for_n_value_1(self):
    self.assertEqual([1, 1], fibonacci_imperative(1))
  
  def test_imperative_fibonacci_returns_fibonacci_less_than_21_for_n_value_30(self):
    self.assertEqual([1, 1, 2, 3, 5, 8, 13, 21], fibonacci_imperative(30))
  
if __name__ == '__main__':
  unittest.main()