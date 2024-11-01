while True:
    try:
        row,column=input().split()
        n=len(row); m=len(column)
        dp=[[0]*(m+1) for i in range(0,n+1)]
        row_mark=[[0]*(m+1) for i in range(0,n+1)]
        col_mark=[[0]*(m+1) for i in range(0,n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                up=dp[i-1][j]
                row_update=-1
                for k in range(col_mark[i-1][j]+1,j+1):
                    if column[k-1]==row[i-1]:
                        up+=1
                        row_update=k
                        break
                left=dp[i][j-1]
                col_update=-1
                for k in range(row_mark[i][j-1]+1,i+1):
                    if row[k-1]==column[j-1]:
                        left+=1
                        col_update=k
                        break
                dp[i][j]=max(left,up)
                if up>left:
                    row_mark[i][j]=row_mark[i-1][j] if row_update==-1 else i
                    col_mark[i][j]=col_mark[i-1][j] if row_update==-1 else row_update
                else:
                    row_mark[i][j]=row_mark[i][j-1] if col_update==-1 else col_update
                    col_mark[i][j]=col_mark[i][j-1] if col_update==-1 else j
        print(dp[n][m])
    except EOFError:
        break