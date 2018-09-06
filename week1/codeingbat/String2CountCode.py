def count_code(str):
  count=0
  for n in range(0, len(str)-3):
    if str[n:n+2]=='co' and str[n+3]=='e':
      count+=1
  return count
