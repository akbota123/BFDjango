#find the runner up score from hackerrank EASY

if __name__ == '__main__':
    import math
    n = int(input())
    arr = set(map(int, input().split()))
    print(sorted(arr, reverse = True)[1])
