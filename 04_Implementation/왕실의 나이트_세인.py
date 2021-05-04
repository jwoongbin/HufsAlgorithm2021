#나이트 위치
location= input()
row= int(location[1])
column= int(ord(location[0])) - int(ord('a')) + 1

#8가지 방향 정의
steps=[(-2,-1), (-1,-2), (1,-2),(2,-1),(2,1), (1,2), (-1,2), (-2,1)]

#각 방향으로 이동 가능한지 확인
result=0
for step in steps:
    #이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    #해당 위치로 이동 가능하면 카운트 증가
    if next_row >=1 and next_row <=8 and next_column >=1 and next_column <=8:
        result +=1

print(result)