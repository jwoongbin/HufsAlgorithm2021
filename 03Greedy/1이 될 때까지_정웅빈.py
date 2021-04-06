n, k = map(int, input().split())

# count = 0
# while n >= 2:
#     if n % k == 0:
#         n = n // k
#     else:
#         n = n - 1
#     count += 1
#
# print(count)

count = 0
while True:

    greedy = (n // k) * k
    count += (n - greedy)

    n = greedy

    if n < k:
        break

    n //= k
    count += 1
    
count += (n-1)
print(count)
