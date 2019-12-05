import unittest
from test.fibonacci.fibonacci_test import FibonacciTest
from timeit import default_timer as timer
from src.fibonacci.fibonacci_memoized import FibonacciMemoized
from src.fibonacci.fibonacci_recursive import FibonacciRecursive


class FibonacciMemoizedTest(FibonacciTest, unittest.TestCase):

  def fibonacci_function(self, position):
    return FibonacciMemoized().fibonacci(position)

  def test_fibonacci_performance(self):
    recursive_function = FibonacciRecursive().fibonacci
    start = timer()
    recursive_function(25)
    recursive_time = timer() - start

    start = timer()
    self.fibonacci_function(25)
    memoized_time = timer() - start

    self.assertLessEqual(memoized_time, 10 * recursive_time)


if __name__ == '__main__':
  unittest.main()
