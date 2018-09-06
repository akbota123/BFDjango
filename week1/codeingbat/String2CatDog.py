def cat_dog(str):
  c_count=0
  d_count=0
  for n in range(len(str)-2):
    if str[n:n+3]=='cat':
      c_count+=1
    if str[n:n+3]=='dog':
      d_count+=1
  return c_count==d_count
