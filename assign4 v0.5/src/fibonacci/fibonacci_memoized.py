from src.fibonacci.fibonacci_recursive import FibonacciRecursive


class FibonacciMemoized:
  fibonacci_memo = {}


  def fibonacci(self, position):
    if position in self.fibonacci_memo:
      return self.fibonacci_memo[position]

    if position < 0: raise ValueError('Invalid Fibonacci position')

    if position in [0, 1]: return 1

    self.fibonacci_memo[position] = FibonacciRecursive().recursive_call(self, position)
    return self.fibonacci_memo[position]
