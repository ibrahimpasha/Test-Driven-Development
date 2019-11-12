from functools import reduce


class FibonacciFunctional:

  def fibonacci(self, position):
    if position < 0: raise ValueError("Invalid Fibonacci position")

    return reduce(
      lambda series, _: (
          series[1], series[0] + series[1]),
          range(0, position - 1),
          (1, 1),
          )[1]
