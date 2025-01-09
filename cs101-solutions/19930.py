from collections import deque
m,n=map(int,input().split())
graph=[[2 for _ in range(0,n+2)]]
for _ in range(0,m):
    graph.append([2]+list(map(int,input().split()))+[2])
graph.append([2 for _ in range(0,n+2)])
def bfs():
    directions={(1,0),(-1,0),(0,1),(0,-1)}
    queue=deque()
    queue.append((1,1))
    step=0
    if graph[1][1]==1: return 0
    while len(queue)>0:
        for i in range(0,len(queue)):
            x,y=queue.popleft()
            for dx,dy in directions:
                u=x+dx; v=y+dy
                if graph[u][v]==1:
                    return step+1
                elif graph[u][v]==0:
                    queue.append((u,v))
                    graph[u][v]=2
        step+=1
    return -1
s=bfs()
if s==-1: print("NO")
else: print(s)