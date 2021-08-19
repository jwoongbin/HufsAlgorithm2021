N = int(input())
data = list(map(int, input().split()))
M = int(input())
target = list(map(int, input().split()))

def binary_search(data, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2

    if data[mid] == target:
        return 1
    elif data[mid] > target:
        return binary_search(data, target, start, mid-1)
    elif data[mid] < target:
        return binary_search(data, target, mid+1, end)

data.sort()
for targets in target:
    print(binary_search(data, targets, 0, len(data)-1))
