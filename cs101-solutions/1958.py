dp=[0]*13
for i in range(1,13):
    min_move=float('inf')
    for k in range(1,i+1):
        min_move=min(min_move,2*dp[i-k]+2**k-1)
    dp[i]=min_move
    print(dp[i])