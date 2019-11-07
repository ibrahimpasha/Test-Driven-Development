import unittest
from src.fibonacci.fibonacci_memoized import fibonacci_memoized


class FibonacciMemoizedTest(unittest.TestCase):
  
  def test_canary(self):
    self.assertTrue(True)
  
  def test_memoized_fibonacci_returns_1_for_position_0(self):
    self.assertEqual(1, fibonacci_memoized(0))
    
  def test_memoized_fibonacci_returns_1_for_position_1(self):
    self.assertEqual(1, fibonacci_memoized(1))
  
  def test_memoized_fibonacci_returns_5_for_position_4(self):
    self.assertEqual(5, fibonacci_memoized(4))

  def test_memoized_fibonacci_returns_20365011074_for_position_50(self):
    self.assertEqual(20365011074, fibonacci_memoized(50))

  def test_memoized_fibonacci_returns_None_for_position_less_than_zero(self):
    with self.assertRaises(ValueError):
      fibonacci_memoized(-1)

if __name__ == '__main__':
  unittest.main()
