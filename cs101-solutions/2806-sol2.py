while True:
    try:
        row,column=input().split()
    except EOFError:
        break
    n=len(row); m=len(column)
    dp=[[0]*(m+1) for i in range(0,n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if row[i-1]==column[j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    print(dp[n][m])