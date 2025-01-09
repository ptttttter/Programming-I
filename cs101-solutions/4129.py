from collections import deque
directions={(0,1),(0,-1),(1,0),(-1,0)}
for _ in range(0,int(input())):
    r,c,k=map(int,input().split())
    maze=[]
    for i in range(0,r):
        maze.append([s for s in input()])
    def bfs():  
        queue=deque(); inq=set()
        for i in range(0,r):
            for j in range(0,c):
                if maze[i][j]=='S':
                    queue.append((i,j))
                    inq.add((i,j,0))
                    maze[i][j]='.'
        time=0
        while queue:
            time+=1
            for l in range(0,len(queue)):
                x,y=queue.popleft()
                for dx,dy in directions:
                    nx,ny=x+dx,y+dy
                    if not(0<=nx<r and 0<=ny<c): continue
                    if (maze[nx][ny]=='.' or (maze[nx][ny]=='#' and time%k==0)) \
                    and (nx,ny,time%k) not in inq:
                        queue.append((nx,ny))
                        inq.add((nx,ny,time%k))
                    if maze[nx][ny]=='E': return time
        return "Oop!"
    print(bfs())