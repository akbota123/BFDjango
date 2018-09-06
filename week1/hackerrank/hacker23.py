#word order from hackerrank MEDIUM

n = int(input())
word = []
count = {}
for _ in range(n):
    w = input()
    if w in count:
        count[w] += 1
    else:
        word.append(w)
        count[w] = 1
print(len(word))
print(*map(lambda w: count[w], word))