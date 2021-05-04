# 맵크기 입력
n, m = map(int, input().split())

# 맵 생성하고 0으로 초기화
d = [[0]*m for _ in range(n)]
# 캐릭터 위치 및 방향 입력
x, y, direction = map(int, input().split())
d[x][y] = 1    # 현재 좌표 방문 처리

# 맵 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    # 정면 타일 좌표 정의
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 정면에 육지인 미방문 타일 존재할 시 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 정면에 방문 타일이 존재하거나 바다일 시
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없을 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있으면
        else:
            break
        turn_time = 0

print(count)