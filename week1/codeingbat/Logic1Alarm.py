def alarm_clock(day, vacation):
  d="7:00"
  weekend="10:00"
  if vacation:
    d="10:00"
    weekend="off"
  if day>0 and day<6:
    return d
  else:
    return weekend
