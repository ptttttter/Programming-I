import sys
data=sys.stdin.read()
lines=data.split()
ans=[]
K=int(lines[0])
row=1
for _ in range(K):
    m,n=int(lines[row]),int(lines[row+1]); row+=2
    h=[]
    height=[[0]*n for i in range(0,m)]
    visited=[[False]*n for i in range(0,m)]
    for i in range(0,m):
        h.append([int(item) for item in lines[row:row+n]]); row+=n
    x,y=int(lines[row]),int(lines[row+1]); row+=2
    p=int(lines[row]); row+=1
    queue=[]
    for i in range(0,p):
        x0,y0=int(lines[row]),int(lines[row+1]); row+=2
        height[x0-1][y0-1]=h[x0-1][y0-1]
        queue.append((x0-1,y0-1))
    #dfs
    while queue:
        i,j=queue.pop()
        visited[i][j]=True
        if (i,j)==(x-1,y-1): break
        directions={(0,1),(0,-1),(1,0),(-1,0)}
        for dx,dy in directions:
            if 0<=i+dx<m and 0<=j+dy<n and height[i][j]>h[i+dx][j+dy]:
                queue.append((i+dx,j+dy))
                height[i+dx][j+dy]=max(height[i+dx][j+dy],height[i][j])
    ans.append(visited[x-1][y-1])     
for answer in ans:
    print("Yes" if answer else "No")           