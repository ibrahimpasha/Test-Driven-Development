import unittest
from test.fibonacci.fibonacci_test import FibonacciTest
from src.fibonacci.fibonacci_imperative import FibonacciImperative


class FibonacciImperativeTest(FibonacciTest, unittest.TestCase):

  def fibonacci_function(self, position):
    return FibonacciImperative().fibonacci(position)


if __name__ == '__main__':
  unittest.main()
