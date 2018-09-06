import math

a=int(input())
b=int(input())

for i in range(a, b + 1):
    t=int
    t=math.sqrt(i)
    if t * t == i:
        print(i)