import unittest
from src.fibonacci.fibonacci_memoized import FibonacciMemoized
from test.fibonacci.common_fibonacci_test import CommonFibonacciTests
from test.fibonacci.performance_timer import performance_time


class FibonacciMemoizedTest(unittest.TestCase):

  def setUp(self):
    self.memoized = FibonacciMemoized()
    self.common_fib = CommonFibonacciTests()

  def test_fibonacci_memoized(self):
    self.common_fib.fibonacci_returns_1_for_position_0(self.memoized)
    self.common_fib.fibonacci_returns_1_for_position_1(self.memoized)
    self.common_fib.fibonacci_returns_2_for_position_2(self.memoized)
    self.common_fib.fibonacci_returns_8_for_position_5(self.memoized)
    self.common_fib.fibonacci_raises_ValueError_position_less_than_zero(self.memoized)

  def test_fibonacci_performance(self):
    minimum, average = performance_time(function=self.memoized.fibonacci, 
                                        position=30,
                                        repeats=5)
    self.assertLess(minimum, 1e-04)
    self.assertLess(average, 1e-04)


if __name__ == '__main__':
  unittest.main()
