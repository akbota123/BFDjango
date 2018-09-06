import math

n=int(input())
s=0
for i in range(1, n+1):
    k=int(input())
    if k==0:
        s=s+1
        
print(s)