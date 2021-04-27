N, M = map(int, input().split())
square = [[0]*M for _ in range(N)]
for i in range(N):
    square[i] = list(map(int, input().split()))

result = 0

# dfs 알고리즘
def solution(x, y):
    square[x][y] = 9
    global result
    global i
    a = [-1, 0, 1, 0]
    b = [0, 1, 0, -1]
    for i in range(4):
        if N-1 >= x + a[i] >= 0 and M-1 >= y + b[i] >= 0:
            if square[x + a[i]][y + b[i]] == 0:
                # 갈 수 있는 방향이 있다면
                solution(x + a[i], y + b[i])

for i in range(N):
    for j in range(M):
        if square[i][j] == 0:
            result += 1
            solution(i, j)

print(result)
for k in range(N):
    print(square[k])