from collections import deque

N, M, K, X = list(map(int, input().split())) # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호

graph = [[] for i in range(M+1)]
print(graph)
for i in range(M):
    x, y = list(map(int,input().split()))
    graph[x].append(y)

print(graph)


def bfs(graph, start, k, dist):
    queue = deque([start])
    d = 0

    while d != k:
        v = queue.popleft()
        d += 1
        for i in graph[v]:
            if not dist[i]:
                dist[i] = d
                queue.append(i)


# 출발 노드로부터 각 노드까지의 거리를 기록
dist = [False] * (N+1)
bfs(graph, X, K, dist)

print(dist)

if not K in dist:
    print('-1')
else:
    for i in range(len(dist)):
        if dist[i] == K:
            print(i)
