n, k = map(int, input().split())
# n과 k를 각각 입력받기

number = 0
count = 0

while True:
    if n % k != 0:
        # n이 k로 나눠지지 않는 경우
        target = n % k
        number += target
        n -= target
    else:
        # n이 k로 나눠지는 경우
        n //= k
        count += 1

        if n == 1:
            number += count
            print(number)
            break
