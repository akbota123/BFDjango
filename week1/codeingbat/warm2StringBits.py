def string_bits(str):
  word=''
  for n in range(0, len(str)):
    if n%2==0:
      word+=str[n]
  return word
