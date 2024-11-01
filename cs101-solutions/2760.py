N=int(input())
triangle=[]
for i in range(0,N):
    line=[0]
    line.extend(list(map(int,input().split())))
    line.append(0)
    triangle.append(line)
dp=[[0]*(j+2) for j in range(1,N+1)]
dp[0][1]=triangle[0][1]
for i in range(1,N):
    for j in range(1,i+2):
        dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]
print(max(dp[N-1]))