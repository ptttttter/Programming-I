r,c=map(int,input().split())
height=[]
for _ in range(0,r): height.append(list(map(int,input().split())))
dp=[[0]*c for _ in range(0,r)]
def dfs(i,j):
    if dp[i][j]>0: return dp[i][j]
    nmax=0
    directions={(1,0),(-1,0),(0,1),(0,-1)}
    for dx,dy in directions:
        x=i+dx; y=j+dy
        if 0<=i+dx<r and 0<=j+dy<c and height[i][j]>height[x][y]:
            nmax=max(nmax,dfs(x,y)) 
    dp[i][j]=1+nmax
    return dp[i][j]
maxlength=1
for i in range(0,r):
    for j in range(0,c):
        maxlength=max(maxlength,dfs(i,j))
print(maxlength)