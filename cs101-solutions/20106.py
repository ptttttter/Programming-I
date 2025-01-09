m,n,p=map(int,input().split())
graph=[]
for i in range(0,m):
    graph.append(list(input().split()))
directions={(0,1),(0,-1),(1,0),(-1,0)}
def bfs(x1,y1,x2,y2):
    from collections import deque
    if graph[x1][y1]=='#' or graph[x2][y2]=='#': return -1
    queue=deque()
    queue.append((x1,y1))
    cost=[[-1]*n for _ in range(m)]
    cost[x1][y1]=0
    cur=float('inf')
    while queue:
        for _ in range(len(queue)):
            x,y=queue.popleft()
            for dx,dy in directions:
                nx=x+dx; ny=y+dy
                if nx<0 or nx>=m or ny<0 or ny>=n: continue
                if graph[nx][ny]=='#': continue
                ncost=cost[x][y]+abs(int(graph[x][y])-int(graph[nx][ny]))
                if ncost<cost[nx][ny] or cost[nx][ny]==-1:
                    cost[nx][ny]=ncost
                    if (nx,ny)==(x2,y2):
                        cur=min(cur,ncost)
                    else:
                        if ncost<cur:
                            queue.append((nx,ny))
    return cost[x2][y2]
while True:
    try:
        x1,y1,x2,y2=map(int,input().split())
        ans=bfs(x1,y1,x2,y2)
        print("NO" if ans==-1 else ans)
    except EOFError:
        break