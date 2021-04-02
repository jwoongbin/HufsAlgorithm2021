n, m = map(int, input().split())

min_data = [0]*m

for i in range(n):
    data = list(map(int, input().split()))
    min_data[i] += min(data)

print(max(min_data))

