def count_hi(str):
  count=0
  for n in range(len(str)-1):
    if str[n:n+2]=='hi':
      count+=1
  return count
