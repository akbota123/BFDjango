def string_splosion(str):
  word=''
  for n in range(0, len(str)+1):
    word+=str[:n]
  return word
