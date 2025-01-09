n=int(input())
a=list(map(int,input().split()))
dp=[[0,0,0] for i in range(0,n+1)]
#dp[i][s], s=0,if rest; 1,if gym; 2,if contest
for i in range(1,n+1):
    state=a[i-1]
    dp[i][0]=min(dp[i-1])+1 #rest update
    dp[i][1]=min(dp[i-1][2],dp[i-1][0]) if state//2==1 else n+1 #gym update
    dp[i][2]=min(dp[i-1][1],dp[i-1][0]) if state%2==1 else n+1 #contest update
print(min(dp[n]))