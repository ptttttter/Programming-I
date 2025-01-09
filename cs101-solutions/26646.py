n,m=map(int,input().split())
plans=[]
for i in range(0,n):
    x,y=map(int,input().split())
    plans.append((x,y))
plans.sort()
dp=[[0 for j in range(0,m+1)] for i in range(0,n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j]=dp[i-1][j]
        left=min(j-plans[i-1][1],plans[i-1][0])
        if left>=0 and j>plans[i-1][0]:
            dp[i][j]=max(dp[i][j],dp[i-1][left]+1)
print(dp[n][m])