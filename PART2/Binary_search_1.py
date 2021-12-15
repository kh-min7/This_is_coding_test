n = int(input())
array = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

array.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid + 1
    return None


for x in find:
    if binary_search(array, x, 0, n - 1) is True:
        print("yes", end=" ")
    else:
        print("no", end=" ")
