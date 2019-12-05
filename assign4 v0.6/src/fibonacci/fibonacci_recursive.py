from src.fibonacci.recusive_call import recursive_call


class FibonacciRecursive:
  def fibonacci(self, position):
    if position < 0: raise ValueError('Invalid Fibonacci position')

    if position in [0, 1]: return 1

    return recursive_call(self, position)

