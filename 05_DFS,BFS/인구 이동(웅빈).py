from collections import deque

N, L, R = list(map(int, input().split())) # 두 나라간의 인구 차이가 L명 이상, R명 이하라면 연합

land = [] # 국가 정보
for i in range(N):
    land.append(list(map(int,input().split())))

print('- 국가 초기 상태')
for lands in land:
    print(lands)


# 인구 이동 -> (연합 국가의 인구 수) / (연합 국가의 수)


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def make_union(x, y, visited): # 연합국 생성
    q = deque([(x, y)])
    human = 0
    united = []
    while q:
        x, y = q.popleft()
        if visited[x][y] == 1: # 이미 방문 했으면
            continue
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < N: # 범위 내 존재
                if [nx, ny] in united: # 이미 가입된 국가라면
                    continue

                if L <= abs(land[x][y]-land[nx][ny]) <= R: # 차이가 L이상 R이하라면
                    q.append((nx, ny))
                    united.append([nx,ny])
                    human += land[nx][ny]

    if len(united) != 0:
        human_migration.append([united, human // len(united)])


count = 0
while(True):

    visited = [[0] * N for i in range(N)]
    # global human_migration
    human_migration = [] # 인구 이동 정보 reset
    for i in range(N):
        for j in range(N):
            make_union(i, j, visited)


    if len(human_migration) == 0: # 더 이상 가능한 인구 이동이 없을 때까지
        break
    else:
        print('인구 이동 정보: ', human_migration)
        print('연합국의 수: ', len(human_migration))

    count += 1
    for human_migrations in human_migration: # 인구 이동
        coordinates, population = human_migrations
        for coordinate in coordinates:
            x, y = coordinate
            land[x][y] = population

    print('- %d번째 인구 이동 후' %count)
    for lands in land:
        print(lands)


print('- 총 인구 이동 일:', count)
