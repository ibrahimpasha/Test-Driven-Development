import unittest
from src.fibonacci.fibonacci_functional import FibonacciFunctional
from test.fibonacci.common_fibonacci_test import CommonFibonacciTests
from test.fibonacci.performance_timer import performance_time

class FibonacciFunctionalTest(unittest.TestCase):

  def setUp(self):
    self.functional = FibonacciFunctional()
    self.common_fib = CommonFibonacciTests()

  def test_fibonacci_functional(self):
    self.common_fib.fibonacci_returns_1_for_position_0(self.functional)
    self.common_fib.fibonacci_returns_1_for_position_1(self.functional)
    self.common_fib.fibonacci_returns_2_for_position_2(self.functional)
    self.common_fib.fibonacci_returns_8_for_position_5(self.functional)
    self.common_fib.fibonacci_raises_ValueError_position_less_than_zero(self.functional)

  def test_fibonacci_performance(self):
    minimum, average = performance_time(function=self.functional.fibonacci, 
                                        position=25, 
                                        repeats=5)
    self.assertLess(minimum, 1e-04)
    self.assertLess(average, 1e-04)

if __name__ == '__main__':
  unittest.main()
