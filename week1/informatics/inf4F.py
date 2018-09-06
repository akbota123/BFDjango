a=input().split()
s=0
for i in range(len(a)-2):
    if int(a[i])<int(a[i+1]) and int(a[i+2])<int(a[i+1]):
        s+=1
print(s)