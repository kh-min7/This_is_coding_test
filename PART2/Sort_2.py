n = int(input())
array = []

for _ in range(n):
    students = input().split()

    array.append((students[0], int(students[1])))

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')