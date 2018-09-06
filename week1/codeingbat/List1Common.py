def common_end(a, b):
  len(a)>=1 and len(b)>=1
  if a[0]==b[0] or a[-1:]==b[-1:]:
    return True
  else:
    return False
