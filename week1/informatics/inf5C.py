x=int(input())
y=int(input())

def xor(x, y):
    return (x and not y)+(y and not x)

print(xor(x, y))