import unittest
from test.fibonacci.fibonacci_test import FibonacciTest
from src.fibonacci.fibonacci_imperative import fibonacci


class FibonacciImperativeTest(FibonacciTest, unittest.TestCase):

  def fibonacci_function(self, position):
    return fibonacci(position)


if __name__ == '__main__':
  unittest.main()
