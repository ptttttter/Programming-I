n=int(input())
*height,=map(int,input().split())
dp=[[0,0] for _ in range(n+1)]
ans=0
for i in range(1,n+1):
    #dp0 从未下山 dp1 有下一步必须下山限制
    dp[i][0]=1
    dp[i][1]=0
    for j in range(1,i):
        if height[i-1]>height[j-1]:
            dp[i][0]=max(dp[i][0],dp[j][0]+1)
        elif height[i-1]<height[j-1]:
            dp[i][1]=max(dp[i][1],max(dp[j])+1)
    ans=max(ans,dp[i][0],dp[i][1])
print(ans)