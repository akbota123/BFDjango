def last2(str):
  count=0
  for n in range(len(str)-2):
    if str[n:n+2]==str[-2:]:
      count+=1
  return count
