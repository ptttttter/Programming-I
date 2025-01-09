from bisect import bisect_left
for _ in range(0,int(input())):
    n,k=map(int,input().split())
    *m,=map(int,input().split())
    *p,=map(int,input().split())
    dp=[[0,0] for i in range(0,n)]
    dp[0]=[0,p[0]]
    for i in range(1,n):
        dp[i][0]=max(dp[i-1][0],dp[i-1][1])
        index=bisect_left(m,m[i]-k)
        dp[i][1]=p[i]+max(dp[index][0],dp[index-1][1])
    print(max(dp[n-1]))