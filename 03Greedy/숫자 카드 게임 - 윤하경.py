# 답
'''
n,m = map(int, input().split())

result=0

for i in range(n): 
    data = list(map(int,input().split()))
    smallest = min(data)
    
    result = max(result, smallest)
    
print(result)
'''

# 내 방식



n,m = map(int, input().split())


result_lst=[]

for i in range(n): 
    data = list(map(int,input().split()))
    result_lst.append(min(data))
    
result = max(result_lst)
    
print('result=',result)

