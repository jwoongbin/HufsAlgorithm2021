n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n - 1]
second = data[n - 2]

           
#if m !=k:
#       result = (first*k+second)*(m//(k+1))+first*(m%(k+1))
#else:
#       result = (first*k) 

count = k * (m//(k+1))
count += m % (k+1)

result = 0
result += count * first
result += (m - count) * second


 
print (result)
