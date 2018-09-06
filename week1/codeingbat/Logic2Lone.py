def lone_sum(a, b, c):
  sum=a+b+c
  if a==b==c:
    return 0
  if a==b:
    return c
  if a==c:
    return b
  if b==a:
    return c
  if b==c:
    return a
  return sum
