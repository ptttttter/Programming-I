n=int(input())
maze=[]
for _ in range(0,n):
    maze.append(list(map(int,input().split())))
def bfs():
    from collections import deque
    queue=deque()
    inq=set()
    for i in range(0,n):
        for j in range(0,n):
            if maze[i][j]==5:
                if len(queue)==0:
                    queue.append((i,j))
                    inq.add((i,j))
                else:
                    shape=(i-queue[0][0],j-queue[0][1])
    directions={(0,1),(0,-1),(1,0),(-1,0)}
    while queue:
        x,y=queue.popleft()
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            mx,my=nx+shape[0],ny+shape[1]
            if 0<=nx<n and 0<=ny<n and 0<=mx<n and 0<=my<n \
            and maze[nx][ny]!=1 and maze[mx][my]!=1 and (nx,ny) not in inq:
                inq.add((nx,ny))
                queue.append((nx,ny))
                if maze[nx][ny]==9 or maze[mx][my]==9:
                    return True
    return False
print("yes" if bfs() else "no")