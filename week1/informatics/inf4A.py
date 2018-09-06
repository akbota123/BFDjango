import math

a=input().split()
n=[]

for i in range(len(a)):
    if i%2==0:
        n.append(a[i])
print(' '.join(n))