def string_match(a, b):
  m=min(len(a), len(b))
  count=0
  for n in range(m-1):
    if a[n:n+2]==b[n:n+2]:
      count+=1
  return count