n,a,b,c=map(int,input().split())
dp=[0]*(n+1)
dp[0]=0
for i in range(1,n+1):
    max_prev=-1
    if i>=a: max_prev=max(max_prev,dp[i-a])
    if i>=b: max_prev=max(max_prev,dp[i-b])
    if i>=c: max_prev=max(max_prev,dp[i-c])
    if max_prev==-1:
        dp[i]=-1
    else:
        dp[i]=1+max_prev
print(dp[n])