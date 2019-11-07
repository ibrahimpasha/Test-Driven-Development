def fibonacci_recursive(position):
  if position < 0: raise ValueError('Invalid Fibonacci position')
  
  if position in [0, 1]: return 1
  
  return fibonacci_recursive(position - 2) + fibonacci_recursive(position - 1)
