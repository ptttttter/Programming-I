import bisect
for _ in range(0,int(input())):
    E,F=map(int,input().split())
    N=int(input())
    coins=[]
    for i in range(0,N):
        coins.append(list(map(int,input().split())))
    coins.sort(key=lambda l:l[1])
    p_MAX=1E10
    dp=[p_MAX]*(F-E+1)
    dp[0]=0
    for w in range(1,F-E+1):
        dp[w]=min([dp[w-coins[i][1]]+coins[i][0] if w>=coins[i][1] else p_MAX for i in range(0,N)])
    if dp[F-E]>=p_MAX:
        print("This is impossible.")
    else:
        print(f"The minimum amount of money in the piggy-bank is {dp[F-E]}.")