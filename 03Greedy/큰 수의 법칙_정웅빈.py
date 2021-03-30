n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]
result = 0

# section = k+1
# sectionValue = first*k + second
# repetition = int(m/section)
# rest = int(m%section)
# result = (sectionValue * repetition) + (first * rest)

result = ((first*k) + second) * int(m/(k+1)) + (first * int(m % (k+1)))

print(result)
