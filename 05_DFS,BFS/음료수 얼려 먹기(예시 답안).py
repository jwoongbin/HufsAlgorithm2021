n, m = map(int, input().split())

# DFS(깊이우선) 함수 정의
def dfs(x, y):

    # OutOfIndex
    if  x < 0 or x >= n or y < 0 or y >= m:
      return False

    # If already visited
    if ice_cube[x][y] == 1:
      return False

    # Make visited
    ice_cube[x][y] = 1

    #상하좌우 각각 DFS 호출
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True


ice_cube = []
for i in range(n):
  ice_cube.append(list(map(int, input())))


count = 1
for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      count += 1

print(count)