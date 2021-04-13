# 왕실의 나이트
'''
moves = [(-2,-1),(-2,1),(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
count=0

pos = list(input())

#print(pos)

string = 'abcdefgh'

for s in string:
    if pos[0]==s:
        pos[0]=string.index(s)+1

x,y = pos[0],int(pos[1])
#print(x,y)

for move in moves:
    nx = x + move[0]
    ny = y + move[1]
    if nx<1 or ny<1 or nx>8 or ny>8:
        continue
    #print(nx,ny,move[0],move[1])
    count+=1
    
print(count)
'''

pos = input()
x = int(ord(pos[0])) - int(ord('a')) +1
y = int(pos[1])

moves = [(-2,-1),(-2,1),(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

count=0
for move in moves:
    nx = x + move[0]
    ny = y + move[1]
    
    if nx<=8 and ny<=8 and nx>=1 and ny>=1:
        count+=1

print(count)

