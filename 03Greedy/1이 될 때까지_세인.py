import time

n, k =map(int, input().split())

start_time = time.time() #측정시작

count = 0
while True:
    if n == 1:
       break
    if n >= k:
        if n % k != 0:
            n -= 1
            count += 1
        else:
            n = n // k
            count += 1
    else:
        n -= 1
        count =+ 1

print(count)

end_time = time.time() #측정종료
print("time :", end_time - start_time) #수행시간 출력