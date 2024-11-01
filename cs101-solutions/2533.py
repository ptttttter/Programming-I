n=int(input())
seq=list(map(int,input().split()))
dp=[1]*n
for i in range(1,n):
    length=0
    for j in range(0,i):
        if seq[j]<seq[i]: length=max(length,dp[j])
    dp[i]=length+1
print(max(dp))