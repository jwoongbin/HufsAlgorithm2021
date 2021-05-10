def cutting(array, m, start, end):

    # 중간 값을 절단기의 높이 h로 설정
    mid = (start + array[end]) // 2

    # 절단된 떡의 길이의 합
    sum = 0

    # 떡 자르기    
    for i in range(end, -1, -1):
        if array[i] < mid:
            break
        else:
            sum += array[i] - mid

    # 절단된 떡의 길이의 합이 m 과 같을 경우
    if sum == m:
        return mid

    # 절단된 떡의 길이의 합이 m 보다 클 경우 오른쪽 부분 탐색
    elif sum > m:
        return cutting(array, m, mid, end)
    # 절단된 떡의 길이의 합이 m 보다 작을 경우 시작점의 길이를 -1씩 감소
    else:
        return cutting(array, m, start-1, end)




# 떡의 개수, 필요한 길이 입력 받기
n,m = list(map(int, input().split()))
array = list(map(int, input().split()))
array.sort()
print(cutting(array, m, 0, n-1))


