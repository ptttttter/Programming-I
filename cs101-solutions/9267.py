N,M=map(int,input().split())
dp=[[0]*(M) for _ in range(0,N+1)]
dp[1][0]=dp[1][1]=1
for i in range(2,N+1): dp[i]=[sum(dp[i-1])]+dp[i-1][0:M-1]
print(sum(dp[N]))