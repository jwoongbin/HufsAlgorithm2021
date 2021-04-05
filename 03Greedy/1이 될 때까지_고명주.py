N, K = map(int, input().split())

i = 0
while N != 1:
  if N % K == 0:
    N = N // K
    i += 1
  else:
    N -= 1
    i += 1
print(i)