n, m = map(int, input().split())
# n과 m을 각각 입력받기

minValue = []

for i in range(n):
    data = list(map(int, input().split()))
    # 각각의 행에 해당하는 값 입력

    minValue.append(min(data))
    # 각각의 행에서 가장 작은 값 탐색 후 추가

maxValue = max(minValue)
# 가장 작은 값들 중 가장 큰 값 탐색

print(maxValue)
