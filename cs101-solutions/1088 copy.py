r,c=map(int,input().split())
height=[]
for _ in range(0,r): height.append(list(map(int,input().split())))
from collections import deque,defaultdict
def neighbour(i,j):
    lst=[]
    directions={(1,0),(-1,0),(0,1),(0,-1)}
    for dx,dy in directions:
        if 0<=i+dx<r and 0<=j+dy<c:
            lst.append((i+dx,j+dy))
    return lst
queue=deque()
deg=defaultdict(int)
for i in range(0,r):
    for j in range(0,c):
        deg[(i,j)]=sum([int(height[i][j]>height[x][y]) for (x,y) in neighbour(i,j)])
        if deg[(i,j)]==0:
            queue.append((i,j))
step=0
while queue:
    for _ in range(0,len(queue)):
        x,y=queue.popleft()
        for nx,ny in neighbour(x,y):
            if height[nx][ny]>height[x][y]:
                deg[(nx,ny)]-=1
                if deg[(nx,ny)]==0:
                    queue.append((nx,ny))
    step+=1
print(step)