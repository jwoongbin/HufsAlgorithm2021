import copy
from collections import deque
from itertools import combinations

N = int(input())

school = []
for i in range(N):
    data = input().split()
    school.append(data)

# S, T, X

empty_space = []
t_coordinates = []
for i in range(N):
    for j in range(N):
        if school[i][j] == 'X':
            empty_space.append((i,j))
        elif school[i][j] == 'T':
            t_coordinates.append((i,j))


cases = list(combinations(empty_space, 3))

def wall_installation(case, school):
    for x, y in case:
        school[x][y] = 'O'

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# DFS 넓이 우선 탐색 -> 선생님 감시
def surveilance(school):

    q = deque(t_coordinates)
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while(True):
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    break

                if school[nx][nx] == 'S':  # 학생인 경우
                    return False

                elif school[nx][ny] == 'T' or school[nx][ny] == 'O':  # 선생님 또는 벽인 경우
                    break
                else:  # school[nx][ny] == 'X' # 아무것도 없는 경우
                    school[nx][ny] = 'T'
                    nx += dx[i]
                    ny += dy[i]
    return True



count = 0
for case in cases:
    new_school = copy.deepcopy(school) # 새로운 학교 생성
    wall_installation(case, new_school) # 임의의 3칸에 벽 설치
    if surveilance(new_school) == True:
        count += 1

if count > 0:
    print('YES')
else:
    print('NO')
