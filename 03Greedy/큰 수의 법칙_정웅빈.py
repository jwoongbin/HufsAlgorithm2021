import time
start_time = time.time() # 측정 시작

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

end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
