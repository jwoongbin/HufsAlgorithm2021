# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기(union 연산)
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1) # 부모 테이블 초기화 > 노드의 개수 만큼

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

for i in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union_parent(parent, a, b)
    elif x == 1:
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a == b:
            print('YES')
        else:
            print('NO')



e
