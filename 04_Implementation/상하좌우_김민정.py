# 좌표 칸 규격
N = int(input())
route = list(input().split()) # 상하좌우

start = [1, 1]

for i in route:
    if i == 'R':
        if start[0] < N: # N보다 작을 경우 우로 이동
            start[0] += 1
    if i == 'L':
        if start[0] > 1: # 1보다 클 경우 좌로 이동
            start[0] -= 1
    if i == 'D':
        if start[1] < N: # n보다 작을 경우 아래로 이동
            start[1] += 1
    if i == 'U':
        if start[1] > 1: #1보다 클 경우 위로 이동
            start[1] -= 1

print(start[1], start[0])