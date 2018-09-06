#finding the percentage from hackerrank EASY

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = sum(scores) / len(scores)
    query_name = input()
    print(format(student_marks[query_name], '.2f'))



