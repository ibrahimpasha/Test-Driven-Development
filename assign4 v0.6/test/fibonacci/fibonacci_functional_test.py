import unittest
from test.fibonacci.fibonacci_test import FibonacciTest
from src.fibonacci.fibonacci_functional import FibonacciFunctional


class FibonacciFunctionalTest(FibonacciTest, unittest.TestCase):

  def fibonacci_function(self, position):
    return FibonacciFunctional().fibonacci(position)

 
if __name__ == '__main__':
  unittest.main()
