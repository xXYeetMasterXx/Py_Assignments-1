def evenlySpaced(a, b, c):
  # insert your logic here
  if b-a == c-b or a-c == b-a or c-a == b-c or c-b == a-c or a-b == c-a or b-c == a-b:
    return True
  else:
    return False
