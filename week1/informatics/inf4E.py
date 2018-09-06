a = [int(i) for i in input().split()]
for i in range(len(a) - 1):
    if (a[i] >= 0 and a[i + 1] >= 0) or (a[i] <= 0 and a[i + 1] <= 0):
        if True:
            print("YES")
            break
        
