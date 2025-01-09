p=1000000007
n,k,d0=map(int,input().split())
paths=[[0]*(d0+1) for j in range(0,n+1)]
paths[0][1]=1
paths[1][1]=1
for j in range(2,n+1):
    for d in range(1,d0+1):
        limit=d
        for i in range(1,k+1):
            if i==d: limit=1
            if i>n: break
            paths[j][d]+=paths[j-i][limit]
            paths[j][d]=paths[j][d]%p
print(paths[n][d0])