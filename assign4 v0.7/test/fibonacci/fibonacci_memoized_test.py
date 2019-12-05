import unittest
from test.fibonacci.fibonacci_test import FibonacciTest
from timeit import default_timer as timer
from src.fibonacci import fibonacci_memoized
from src.fibonacci import fibonacci_recursive


class FibonacciMemoizedTest(FibonacciTest, unittest.TestCase):

  def fibonacci_function(self, position):
    return fibonacci_memoized.fibonacci(position)


  def test_fibonacci_performance(self):
    def execution_time(fibonacci):
      start = timer()
      fibonacci(25)
      return timer() - start

    self.assertLessEqual(execution_time(fibonacci_memoized.fibonacci),
                         10 * execution_time(fibonacci_recursive.fibonacci))


if __name__ == '__main__':
  unittest.main()
