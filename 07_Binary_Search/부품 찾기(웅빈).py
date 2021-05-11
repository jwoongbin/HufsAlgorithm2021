def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        # 중간 값이 타켓보다 클 경우 왼쪽 탐색
        elif array[mid] > target:
            end = mid-1

        # 중간 값이 타켓보다 작을 경우 오른쪽 탐색
        else:
            start = mid+1

    return None


n = int(input())
array1 = list(map(int, input().split()))
array1.sort()

m = int(input())
array2 = list(map(int, input().split()))


for i in array2:

        result = binary_search(array, i, 0, n-1)

        if result == None:
            print('no', end =' ')
        else:
            print('yes', end= ' ')
