n, m = list(map(int, input().split()))
weight = list(map(int, input().split()))

result = 0
for i in range(len(weight)):
    for j in range(i+1, len(weight)):
        if weight[i] == weight[j]:
            continue
        else:
            result += 1

print(result)
