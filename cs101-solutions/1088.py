r,c=map(int,input().split())
height=[]
for _ in range(0,r): height.append(list(map(int,input().split())))
from collections import deque
def neighbour(i,j):
    lst=[]
    directions={(1,0),(-1,0),(0,1),(0,-1)}
    for dx,dy in directions:
        if 0<=i+dx<r and 0<=j+dy<c:
            lst.append((i+dx,j+dy))
    return lst
queue=deque()
for i in range(0,r):
    for j in range(0,c):
        if height[i][j]<=min([height[x][y] for (x,y) in neighbour(i,j)]):
            queue.append((i,j))
step=0
while queue:
    inq=set()
    for _ in range(0,len(queue)):
        x,y=queue.popleft()
        for nx,ny in neighbour(x,y):
            if height[nx][ny]>height[x][y] and (nx,ny) not in inq:
                queue.append((nx,ny))    
                inq.add((nx,ny))
    step+=1
print(step)