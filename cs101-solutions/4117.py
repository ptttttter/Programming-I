input_list=[]
while True:
    try:
        input_list.append(int(input()))
    except EOFError:
        break
n=max(input_list)
dp=[[1]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dp[i][0]=0
    for m in range(1,i+1):
        dp[i][m]=0
        for k in range(1,m+1):
            dp[i][m]+=dp[i-k][k]
    for m in range(i+1,n+1):
        dp[i][m]=dp[i][i]
for input_num in input_list:
    print(dp[input_num][input_num])
