from collections import deque

n, m = map(int, input().split())

maze = []
for i in range(n):
  maze.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ['상', '하', '좌', '우']

# BFS(넓이우선) 함수 정의
def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        x, y = queue.popleft()
        print((x, y), end=' : ')
        print(maze[x][y], end=', ')

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 탐색
        for i in range(len(move_types)):
                nx = x + dx[i]
                ny = y + dy[i]

                # OutOfIndex
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue

                # There's monster
                if maze[nx][ny] == 0:
                    continue

                # If not visited
                if maze[nx][ny] == 1:
                    maze[nx][ny] = maze[x][y] + 1 # 자기 자신에서 1을 더한 값으로 저장
                    queue.append((nx, ny))

    # return maze[n-1][m-1]


print(bfs(0, 0))