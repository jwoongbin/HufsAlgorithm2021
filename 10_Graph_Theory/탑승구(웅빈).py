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

G = int(input())
P = int(input())
plane = [0] * (P + 1)
for i in range(1, P+1):
    plane[i] = int(input())

parent = [0] * (G + 1)
# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, G + 1):
    parent[i] = i

result = 0
for i in range(1, P+1): # 비행기의 개수 만큼 도킹 시도

    if parent[plane[i]] != 0:
        result += 1 # 도킹
        union_parent(parent, parent[plane[i]], parent[plane[i]]-1) # 해당 집합과 왼쪽에 있는 집합을 합치기
    else:
        break

print(result)
