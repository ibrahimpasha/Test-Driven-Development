import unittest
from src.fibonacci.fibonacci_imperative import fibonacci_imperative


class FibonacciImperativeTest(unittest.TestCase):
  
  def test_canary(self):
    self.assertTrue(True)
  
  def test_imperative_fibonacci_returns_1_for_position_0(self):
    self.assertEqual(1, fibonacci_imperative(0))
    
  def test_imperative_fibonacci_returns_1_for_position_1(self):
    self.assertEqual(1, fibonacci_imperative(1))
  
  def test_imperative_fibonacci_returns_5_for_position_4(self):
    self.assertEqual(5, fibonacci_imperative(4))

  def test_imperative_fibonacci_returns_21_for_position_7(self):
    self.assertEqual(21, fibonacci_imperative(7))

  def test_imperative_fibonacci_returns_None_for_position_less_than_zero(self):
    with self.assertRaises(ValueError):
      fibonacci_imperative(-1)

if __name__ == '__main__':
  unittest.main()
