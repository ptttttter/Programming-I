n=int(input())
*a,=map(int,input().split())
cnt_pos=0
neg=[]; curr_pos=[]
sum_pos=0
for item in a:
    if item>=0:
        cnt_pos+=1
        sum_pos+=item
    else:
        neg.append(-item)
        curr_pos.append(sum_pos)

m=len(neg)
dp=[[-1]*(m+1) for _ in range(0,m+1)]
dp[0][0]=0
for i in range(1,m+1):
    delta=curr_pos[0] if i==1 else curr_pos[i-1]-curr_pos[i-2]
    dp[i][0]=curr_pos[i-1]
    for j in range(1,i+1):
        if dp[i-1][j]>=0 or dp[i-1][j-1]>=0:
            max_prev=float("-inf")
            if dp[i-1][j]>=0: max_prev=max(max_prev,dp[i-1][j])
            if dp[i-1][j-1]>=0: max_prev=max(max_prev,dp[i-1][j-1]-neg[i-1])
            dp[i][j]=delta+max_prev
        else:
            dp[i][j]=-1
max_neg=0
for j in range(m,-1,-1):
    if dp[m][j]>=0:
        max_neg=j; break
print(cnt_pos+max_neg)