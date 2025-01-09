for _ in range(0,int(input())):
    n,m=map(int,input().split())
    chess=[]
    for i in range(0,n):
        chess.append([1 if s=='W' else 0 for s in input()])
    def dfs(i,j):
        directions={(1,1),(1,0),(1,-1),(-1,1),(-1,0),(-1,-1),(0,1),(0,-1)}
        area=1
        chess[i][j]=0
        for dx,dy in directions:
            x=i+dx; y=j+dy
            if 0<=x<n and 0<=y<m and chess[x][y]:
                area+=dfs(x,y)
        return area
    area_max=0
    for i in range(0,n):
        for j in range(0,m):
            if chess[i][j]==1:
                area_max=max(area_max,dfs(i,j))
    print(area_max)