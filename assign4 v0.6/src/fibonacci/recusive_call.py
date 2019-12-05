def recursive_call(fib_obj, position):
  return fib_obj.fibonacci(position - 2) + fib_obj.fibonacci(position - 1)