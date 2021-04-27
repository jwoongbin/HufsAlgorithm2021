from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

# 방향
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# BFS
def maze():
    queue = deque()

    queue.append((0, 0)) #시작점
    # 다 찾을 때까지
    while(queue):
        (x, y) = queue.popleft()

        # 방향 확인
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            # 범위 확인
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= M:
                continue
            # 벽 확인
            if graph[next_x][next_y] == 0:
                continue
            # 처음 방문 시 거리 증가
            if graph[next_x][next_y] == 1:
                graph[next_x][next_y] = graph[x][y] + 1
                queue.append((next_x, next_y))
    return graph[N-1][M-1]

print(maze())

