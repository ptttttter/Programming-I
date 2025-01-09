t=int(input())
for _ in range(0,t):
    n,m,x,y=map(int,input().split())
    s=[[False for j in range(0,m)] for i in range(0,n)]
    ct,path=0,0
    def dfs(x,y):
        global ct,path
        if x<0 or x>=n or y<0 or y>=m: return
        if s[x][y]==True: return
        s[x][y]=True; ct+=1
        if ct==m*n:
            path+=1
        directions={(1,-2),(1,2),(-1,-2),(-1,2),(-2,1),(-2,-1),(2,1),(2,-1)}
        for dx,dy in directions:
            dfs(x+dx,y+dy)
        s[x][y]=False; ct-=1
    dfs(x,y)
    print(path)