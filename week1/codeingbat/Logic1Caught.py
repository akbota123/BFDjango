def caught_speeding(speed, is_birthday):
  s=0
  if is_birthday:
    s=5
  if speed<=60+s:
    return 0
  elif speed>=81+s:
    return 2
  else:
    return 1
