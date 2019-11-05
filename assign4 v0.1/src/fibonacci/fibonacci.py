def fibonacci_imperative(n):
  if n == 0: return 0
  a, b = 1, 1
  output = [a]
  while b <= n:
    output.append(b)
    a, b = b, a + b
  return output

