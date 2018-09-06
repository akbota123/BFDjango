a=input()
b=input()
c=input()
d=input()
k=int
def min_number(k):
    return min(a, min(b, min(c, d)))

print(min_number(k))