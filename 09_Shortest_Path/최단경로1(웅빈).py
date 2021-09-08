INF = int(1e9)

# 정점(노드)의 개수와 간선의 개수 입력받기
N, M = map(int, input().split())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(M):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = input().split()
    # 'A' -> 1, 'Z' -> 26
    graph[ord(a)-64][ord(b)-64] = int(c)
    graph[ord(b)-64][ord(a)-64] = int(c)

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# x에서 y로 가는 최단경로 출력
x, y = input().split()
if graph[ord(x)-64][ord(y)-64] == INF:
    print('-1')
else:
    print(graph[ord(x)-64][ord(y)-64])
