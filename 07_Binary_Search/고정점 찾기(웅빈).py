# 고정점: 그 값이 인덱스와 동일한 원소 찾기 -> target

N = int(input())
data = list(map(int, input().split()))

def binary_search(array, start, end):
    if start > end:
        return -1

    mid = (start+end) // 2
    if array[mid] == mid:
        return mid

    elif array[mid] > mid: # 중간값이 인덱스보다 클 경우
        return binary_search(array, start, mid-1) # 왼쪽 탐색

    else: # 중간값이 인덱스보다 작을 경우
        return binary_search(array, mid+1, end) # 오른쪽 탐색


print(binary_search(data, 0, len(data)-1))




