import unittest

class CommonFibonacciTests(unittest.TestCase):

  def test_canary(self):
    self.assertTrue(True)

  def fibonacci_returns_1_for_position_0(self, fib_object):
    self.assertEqual(1, fib_object.fibonacci(0))

  def fibonacci_returns_1_for_position_1(self, fib_object):
    self.assertEqual(1, fib_object.fibonacci(1))

  def fibonacci_returns_2_for_position_2(self, fib_object):
    self.assertEqual(2, fib_object.fibonacci(2))

  def fibonacci_returns_8_for_position_5(self, fib_object):
    self.assertEqual(8, fib_object.fibonacci(5))

  def fibonacci_raises_ValueError_position_less_than_zero(self, fib_object):
    with self.assertRaises(ValueError):
      fib_object.fibonacci(-1)

