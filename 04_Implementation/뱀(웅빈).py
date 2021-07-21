from collections import deque

N = int(input())
K = int(input())

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

def turn_right():
    global direction
    direction += 1
    if direction == 4:
        direction = 0

# 게임판 생성
board = []
for i in range(N+1):
    board.append([0]*(N+1))


# 사과의 위치 입력받기
for i in range(K):
    x, y = list(map(int,input().split()))
    if (x, y) == (1, 1):
        print('1행 1렬에는 사과가 있어서는 안됩니다.')
        break
    else:
        board[x][y] = 1

for i in range(len(board)):
    print(board[i])


# 뱀의 방향 전환 횟수와 정보 입력받기
L = int(input())
times = {}
for i in range(L):
    X, C = input().split()
    times[int(X)] = C

print(times)




# 북동서남
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 뱀의 시작 위치와 방향 설정
x, y = 1, 1
board[x][y] = '-'
direction = 1 # 시작 시 뱀의 방향은 오른쪽(동쪽)

time = 0
snake = deque() # 뱀의 동선 기록
snake.append([x, y])
while(True):
    # 향하는 방향을 향해 이동
    nx = x + dx[direction]
    ny = y + dy[direction]

    #  뱀이 게임판 밖으로 나가거나 자기 자신을 만나면 종료
    if (nx < 1 or ny < 1 or nx > N or ny > N) or (board[nx][ny] == '-'):
        time += 1
        break

    # 게임 진행
    # 사과가 있으면 머리 길이 늘이기
    if board[nx][ny] == 1:
        board[nx][ny] = '-'
        snake.append([nx,ny])
    # 사과가 없으면 머리는 늘이고 꼬리는 자르기
    else:
        board[nx][ny] = '-'
        snake.append([nx, ny])
        # 꼬리 자르기
        rootx, rooty = snake.popleft() 
        board[rootx][rooty] = 0
    time += 1

    # 방향 전환
    if time in times.keys():
        if times[time] == 'L':
            turn_left()
        else:
            turn_right()
    # 좌표 갱신
    x, y = nx, ny


print(time)
