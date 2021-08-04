from itertools import permutations

from collections import deque
# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램
# 연산의 결과는 언제나 +- 10억
# 최대값 > - // + *
# 최솟값 > + // - *
# 음수를 양수로 나눌때는 음수를 양수로 바꾼 뒤 연산을 수행하고 그 몫을 다시 음수로 변경
# 연산자 우선순위 고려하지 않음
N = int(input())

data = list(map(int,input().split()))
print(data)

opr_data = list(map(int, input().split())) # +, -, *, //
temp_opr = ['+', '-', '*', '/']

opr = []
for i in range(4):
    for j in range(opr_data[i]):
        opr.append(temp_opr[i])

print('끼워 넣을 연산자:', opr)

# (N-1)개로 구성된 연산자의 조합을 생성 (중복을 허용 -> product)
# cases = list(product(opr, repeat=(N-1)))

cases = list(permutations(opr, N-1))
print('%d개의 조합이 생성됨' %(len(cases)))

global results # 각각의 경우의 수를 저장
results = []

q = deque(cases) # 큐를 사용하여 경우의 수를 하나씩 수행
while q:
    oprs = q.popleft()
    result = data[0]
    for i in range(len(oprs)):
        if oprs[i] == '+':
            result += data[i+1]
        elif oprs[i] == '-':
            result -= data[i+1]
        elif oprs[i] == '*':
            result *= data[i+1]
        else: # oprs[i] == '/'
            if result > 0:
                result //= data[i+1]
            else:
                result = -(-result // data[i+1])
    results.append(result)

print('최대값 =', max(results))
print('최솟값 =', min(results))



