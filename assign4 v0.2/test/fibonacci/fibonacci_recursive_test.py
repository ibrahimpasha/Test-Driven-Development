import unittest
from src.fibonacci.fibonacci_recursive import fibonacci_recursive


class FibonacciRecursiveTest(unittest.TestCase):
  
  def test_canary(self):
    self.assertTrue(True)
  
  def test_recursive_fibonacci_returns_1_for_position_0(self):
    self.assertEqual(1, fibonacci_recursive(0))
    
  def test_recursive_fibonacci_returns_1_for_position_1(self):
    self.assertEqual(1, fibonacci_recursive(1))
  
  def test_recursive_fibonacci_returns_5_for_position_4(self):
    self.assertEqual(5, fibonacci_recursive(4))

  def test_recursive_fibonacci_returns_21_for_position_7(self):
    self.assertEqual(21, fibonacci_recursive(7))

  def test_recursive_fibonacci_returns_None_for_position_less_than_zero(self):
    with self.assertRaises(ValueError):
      fibonacci_recursive(-1)

if __name__ == '__main__':
  unittest.main()
