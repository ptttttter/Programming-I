import math
t=int(input())
for _ in range(0,t):
    n=int(input())
    sum=n*(n+1)//2
    N=math.floor(math.log2(n))
    ans=sum-2*(math.pow(2,N+1)-1)
    print("%d"%ans)