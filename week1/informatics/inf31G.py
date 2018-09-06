import math
x=int(input())
i=2
while i<=x and x%i!=0:
    i+=1
else:
    print(i)