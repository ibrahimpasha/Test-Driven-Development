import unittest
from test.fibonacci.common_fibonacci_test import CommonFibonacciTests
from src.fibonacci.fibonacci_recursive import FibonacciRecursive
from test.fibonacci.performance_timer import performance_time


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
    
  def test_fibonacci_performance(self):
    minimum, average = performance_time(function=self.recursive.fibonacci, 
                                        position=30,
                                        repeats=5)
    self.assertLess(minimum, 5.0)
    self.assertLess(average, 4.5)


if __name__ == '__main__':
  unittest.main()
