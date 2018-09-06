a=input().split()
n=[]
for i in a:
    if int(i)%2==0:
        n.append(i)
print(' '.join(n))