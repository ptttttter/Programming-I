for _ in range(0,int(input())):
    M,N=map(int,input().split())
    dp=[[1]*(M+1)]+[[0]*(M+1) for _ in range(1,M+1)]
    for n in range(1,N+1):
        for m in range(M,0,-1):
            for l in range(M,0,-1):
                dp[m][l]=0
                for i in range(0,l+1):
                    if m-i>=0: dp[m][l]+=dp[m-i][i]
                    else: break
    print(dp[M][M])