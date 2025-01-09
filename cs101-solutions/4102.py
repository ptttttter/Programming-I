N,M,K=map(int,input().split())
dp=[[0]*(K+1) for _ in range(0,N+1)]
for _ in range(0,N+1): dp[_][0]=M
for i in range(0,K):
    cost,dmg=map(int,input().split()) 
    #看到第i个小精灵后，更新整个dp表
    for n in range(N,-1,-1):
        for k in range(i+1,0,-1):
            if n>=cost: dp[n][k]=max(dp[n][k],dp[n-cost][k-1]-dmg)
for k in range(K,-1,-1):
    if dp[N][k]!=0:
        print(k,dp[N][k])
        break