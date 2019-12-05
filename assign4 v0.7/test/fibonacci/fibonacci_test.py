class FibonacciTest:

  def test_canary(self):
    self.assertTrue(True)

  def test_fibonacci_returns_1_for_position_0(self):
    self.assertEqual(1, self.fibonacci_function(0))

  def test_fibonacci_returns_1_for_position_1(self):
    self.assertEqual(1, self.fibonacci_function(1))

  def test_fibonacci_returns_2_for_position_2(self):
    self.assertEqual(2, self.fibonacci_function(2))

  def test_fibonacci_returns_8_for_position_5(self):
    self.assertEqual(8, self.fibonacci_function(5))

  def test_fibonacci_raises_ValueError_position_less_than_zero(self):
    with self.assertRaises(ValueError):
      self.fibonacci_function(-1)

