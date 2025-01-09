import sys
n,k=map(int,input().split())
if k>n**2: print(-1);sys.exit()
rest=k
mark=[[0 for j in range(0,n)] for i in range(0,n)]
for i in range(0,n):
    for j in range(i,n):
        if rest==0: break
        if i==j:
            rest-=1
            mark[i][j]=1
        else:
            if rest>=2:
                rest-=2
                mark[i][j]=mark[j][i]=1 
            else:
                break   
for i in range(0,n):
    print(*mark[i],sep=' ')