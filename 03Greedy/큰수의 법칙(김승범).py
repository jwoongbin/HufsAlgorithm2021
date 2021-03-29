n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]
result = 0

result = int(m/(k+1))*(first*k + second) + (m % (k+1))*first


print(result)
