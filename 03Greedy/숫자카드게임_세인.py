import time

n, m =map(int, input().split())

start_time = time.time() #측정시작

result=0
min_value= list()

for i in range(n):
 data= list(map(int,input().split())) #한줄씩 저장
 min_value.append(min(data)) #가장 작은 수 구하기

result=max(min_value)
print(result)

end_time = time.time() #측정종료
print("time :", end_time - start_time) #수행시간 출력