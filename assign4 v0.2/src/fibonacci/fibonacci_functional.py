from functools import reduce


def fibonacci_functional(position):
  if position < 0: raise ValueError('Invalid Fibonacci position')
  
  if position in [0, 1]: return 1
  
  fibonacci_list = [1, 1]
  for _ in range(position - 1):
    fibonacci_list += [reduce(lambda previous, current: previous + current,
                              fibonacci_list[-2:])]
  
  return fibonacci_list[-1]
