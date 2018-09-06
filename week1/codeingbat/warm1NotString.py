#not string

def not_string(str):
  a=str.split("not")
  if len(a)>1 and a[0]=="":
    return str
  return "not " + str
