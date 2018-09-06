#lists from hackerrank EASY

N = int(input())
list = []
for i in range(N):
    command, *args = input().split()
    if command == 'print':
        print(list)
    else:
        getattr(list, command)(*(int(x) for x in args))

