N, M = map(int,input().split())
N_list = [[int(x) for x in input().split()]for y in range(N)]

max_value = 0
for i in range(N):
  if min(N_list[i]) > max_value:
    max_value = min(N_list[i])

print(max_value)