def binary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(input())
array = list(map(int, input().split()))

for x in array:
    result = binary_search(array, 0, n - 1)

if result is not None:
    print(result)
else:
    print(-1)
