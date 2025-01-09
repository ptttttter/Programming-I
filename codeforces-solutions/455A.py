n=int(input())
a_list=list(map(int,input().split()))
b=max(a_list)
cnt=[0]*(b+1)
for item in a_list:
    cnt[item]+=1
dp=[[0,0] for _ in range(0,b+1)] #dp[a][0(1)] maximum of that<=a when a not chosen(chosen)
for a in range(1,b+1):
    dp[a][0]=max(dp[a-1][0],dp[a-1][1])
    dp[a][1]=a*cnt[a]+dp[a-1][0]
print(max(dp[b][0],dp[b][1]))