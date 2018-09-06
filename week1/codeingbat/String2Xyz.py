def xyz_there(str):
  for n in range(len(str)):
    if str[n]!='.' and str[n+1:n+4]=='xyz':
      return True
    if str[0:3]=='xyz':
      return True
  return False
