n, m, k = map(int, input().split())
lst = list(map(int, input().split()))
answer = 0

lst.sort(reverse = True) #오름차순으로 정렬
# print(lst)

# 가장 큰 값
first = lst[0]
# 그 다음 큰 값
second = lst[1]

while True:
    for i in range(k):
        if m == 0:
            break
        answer += first # 가장 큰 값 k만큼 더해 줌
        m -= 1 # 전체 더하는 횟수 차감

    if m == 0:
        break
    answer += second #두 번째로 큰 값 더함
    m -= 1 # 전체 더하는 횟수 차감 후 while문 반복

print(answer)