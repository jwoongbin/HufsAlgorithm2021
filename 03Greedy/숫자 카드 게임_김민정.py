n, m = map(int, input().split())

answer = 0
row_min = []

for i in range(n):
    row = list(map(int, input().split()))
    row_min.append(min(row))

answer = max(row_min)

print(answer)