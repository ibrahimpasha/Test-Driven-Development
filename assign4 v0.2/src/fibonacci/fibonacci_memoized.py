fibonacci_memo = {}

def fibonacci_memoized(position):
  if position in fibonacci_memo:
    return fibonacci_memo[position]
  
  if position < 0: raise ValueError('Invalid Fibonacci position')
  
  if position in [0, 1]: return 1
  
  fibonacci_memo[position] = fibonacci_memoized(position - 2) + fibonacci_memoized(position - 1)
  
  return fibonacci_memo[position]
