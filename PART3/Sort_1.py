n = int(input())
array = []
for _ in range(n):
    student = input().split()

    array.append((student[0], int(student[1]), int(student[2]), int(student[3])))

array = sorted(array, key=lambda a: (-a[1], a[2], -a[3], a[0]))
for x in array:
    print(x[0])