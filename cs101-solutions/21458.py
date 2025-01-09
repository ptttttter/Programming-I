#类似小偷背包 做二维dp
T,n=map(int,input().split())
t=[];w=[]
for i in range(0,n):
    ti,wi=map(int,input().split())
    t.append(ti); w.append(wi)
dp=[[-1]*(T+1) for _ in range(0,n+1)]#健身时间为t分钟，前i个项目 dp[i][t]
dp[0][0]=0
for i in range(1,n+1):
    for time in range(0,T+1):
        j=i-1
        if time-t[j]<0 or dp[i-1][time-t[j]]==-1:
            dp[i][time]=dp[i-1][time]
        else:
            dp[i][time]=max(dp[i-1][time],dp[i-1][time-t[j]]+w[j])
print(dp[n][T])