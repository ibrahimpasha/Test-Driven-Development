class FibonacciRecursive:

  def recursive_call(self, fib_obj, position):
    return fib_obj.fibonacci(position - 2) + fib_obj.fibonacci(position - 1)

  def fibonacci(self, position):
    if position < 0: raise ValueError('Invalid Fibonacci position')

    if position in [0, 1]: return 1

    return self.recursive_call(self, position)

