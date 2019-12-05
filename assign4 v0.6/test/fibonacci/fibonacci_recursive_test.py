import unittest
from test.fibonacci.fibonacci_test import FibonacciTest
from src.fibonacci.fibonacci_recursive import FibonacciRecursive


class FibonacciRecursiveTest(FibonacciTest, unittest.TestCase):

  def fibonacci_function(self, position):
    return FibonacciRecursive().fibonacci(position)


if __name__ == '__main__':
  unittest.main()
