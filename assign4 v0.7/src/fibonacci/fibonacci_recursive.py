def fibonacci(position, dispatch=None):
  if position < 0: raise ValueError('Invalid Fibonacci position')

  if position in [0, 1]: return 1

  if not dispatch: dispatch = fibonacci

  return dispatch(position - 2) + dispatch(position - 1)
