from src.fibonacci import fibonacci_recursive


def fibonacci(position, cache=dict()):
  if position in cache:
    return cache[position]

  cache[position] = fibonacci_recursive.fibonacci(position, fibonacci)

  return cache[position]
