n, m, k = map(int, input().split())
num = list(map(int, input().split()))
sort_num = sorted(num, reverse=True) #오름차순 정렬
count = 0 #횟수 카운트
result = 0 #결과 저장

while True:
  for i in range(k): #연속 반복 가능 횟수 k번
    if count == m: #만약 횟수가 m번이 되면 break
      break
    result += sort_num[0] #가장 큰 값 더하기
    count += 1 #횟수 카운트 +1
  if count == m: #만약 횟수가 m번이 되면 break
    break
  result += sort_num[1] #두번째로 큰 값 더하기
  count += 1 #횟수 카운트 +1

print(result)