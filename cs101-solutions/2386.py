n,m=map(int,input().split())
field=[]
def pool_search(i,j):
    direct=[[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,1],[-1,0],[-1,-1]]
    field[i][j]=False
    for direct_x,direct_y in direct:
        x=i+direct_x; y=j+direct_y
        if 0<=x<n and 0<=y<m:
            if field[x][y]:
                pool_search(x,y)
for i in range(0,n):
    field.append([True if s=='W' else False for s in input()])
cnt=0
for i in range(0,n):
    for j in range(0,m):
        if field[i][j]:
            #search the whole pool
            pool_search(i,j)
            cnt+=1
print(cnt)