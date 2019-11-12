import unittest
from src.fibonacci.fibonacci_imperative import FibonacciImperative
from test.fibonacci.common_fibonacci_test import CommonFibonacciTests
from test.fibonacci.performance_timer import performance_time

class FibonacciImperativeTest(unittest.TestCase):

  def setUp(self):
    self.imperative = FibonacciImperative()
    self.common_fib = CommonFibonacciTests()

  def test_fibonacci_imperative(self):
    self.common_fib.fibonacci_returns_1_for_position_0(self.imperative)
    self.common_fib.fibonacci_returns_1_for_position_1(self.imperative)
    self.common_fib.fibonacci_returns_2_for_position_2(self.imperative)
    self.common_fib.fibonacci_returns_8_for_position_5(self.imperative)
    self.common_fib.fibonacci_raises_ValueError_position_less_than_zero(self.imperative)

  def test_fibonacci_performance(self):
    minimum, average = performance_time(function=self.imperative.fibonacci, 
                                        position=30,
                                        repeats=5)
    self.assertLess(minimum, 1e-04)
    self.assertLess(average, 1e-04)

if __name__ == '__main__':
  unittest.main()
