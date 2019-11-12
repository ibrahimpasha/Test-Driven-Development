import unittest
from src.fibonacci.fibonacci_recursive import FibonacciRecursive
from test.fibonacci.common_fibonacci_test import CommonFibonacciTests


class FibonacciRecursiveTest(unittest.TestCase):

  def setUp(self):
    self.recursive = FibonacciRecursive()
    self.common_fib = CommonFibonacciTests()

  def test_fibonacci_recursive(self):
    self.common_fib.fibonacci_returns_1_for_position_0(self.recursive)
    self.common_fib.fibonacci_returns_1_for_position_1(self.recursive)
    self.common_fib.fibonacci_returns_2_for_position_2(self.recursive)
    self.common_fib.fibonacci_returns_8_for_position_5(self.recursive)
    self.common_fib.fibonacci_raises_ValueError_position_less_than_zero(self.recursive)

if __name__ == '__main__':
  unittest.main()
