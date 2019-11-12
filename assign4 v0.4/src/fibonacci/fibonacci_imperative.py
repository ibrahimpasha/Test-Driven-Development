class FibonacciImperative:

  def fibonacci(self, position):
    if position < 0: raise ValueError('Invalid Fibonacci position')

    if position in [0, 1]: return 1

    previous, current = 1, 1

    for _ in range(position - 1):
      previous, current = current, previous + current

    return current
