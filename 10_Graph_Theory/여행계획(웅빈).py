def find_parent(parent, x):
    #루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split()) # 여행지의 수, 여행 계획에 속한 도시의 수
graph = []
for i in range(1, N+1):
    datas = list(map(int, input().split()))
    for j in range(0, N):
        if datas[j] == 1:
            graph.append((i, j+1))

print(graph)

routine = list(map(int,input().split()))

parent = [0] * (N + 1) # 부모 테이블 초기화
# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, N + 1):
    parent[i] = i

# Union 연산을 각각 수행
for graphs in graph:
    a, b = graphs
    union_parent(parent, a, b)

print('parent:', parent)
print('routine:', routine)

flag = "Yes"
for i in range(1, len(routine)):
    if parent[routine[i-1]] == parent[routine[i]]:
        continue
    else:
        flag = "No"

print(flag)
