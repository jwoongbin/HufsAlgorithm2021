N,K = map(int, input().split())

result = 0

while N>0:
    
    if N%K == 0:
        N = N//K 
        result+=1
        #print(N,  result)
        
    else:
        N-=1
        result+=1
        #print(N, result)
        
print(result-1)
