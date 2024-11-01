k=int(input())
height=list(map(int,input().split()))
dp=[1]*k
for i in range(0,k):
    max_num=0
    for j in range(0,i):
        if height[i]<=height[j]:
            max_num=max(max_num,dp[j])
    dp[i]=1+max_num
print(max(dp))