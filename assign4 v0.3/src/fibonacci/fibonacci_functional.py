from functools import reduce


def sum(prev_next_tuple, _):
  prev, next = prev_next_tuple
  return (next, prev + next)

def fibonacci_functional(position):
  if position < 0: raise ValueError('Invalid Fibonacci position')

  return reduce(sum, range(0, position - 1), (1, 1))[1]

