N = int(input())

data = []
for i in range(N):
    data.append(tuple((input().split())))

print(data)

data.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for datas in data:
    print(datas[0])
