if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    s=0
    avg= float()
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks[query_name]:
        s += i
    avg = s / len(student_marks[query_name])
    print("%.2f" %avg)
