N,B=map(int,input().split())
price=list(map(int,input().split()))
weight=list(map(int,input().split()))
dp=[[0]*(B+1) for i in range(0,N+1)] #dp[n][w]
for i in range(1,N+1):
    for w in range(1,B+1):
        if w>=weight[i-1]:
            dp[i][w]=max(dp[i-1][w],dp[i-1][w-weight[i-1]]+price[i-1])
        else:
            dp[i][w]=dp[i-1][w]
print(dp[N][B])