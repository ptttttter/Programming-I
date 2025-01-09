n,m=map(int,input().split())
field=[]
def pool_search(i,j):
    direct=[(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]
    stack=[(i,j)]
    field[i][j]=False
    while stack:
        x,y=stack.pop()
        for direct_x,direct_y in direct:
            x_new=x+direct_x
            y_new=y+direct_y
            if x_new<0 or x_new>=n or y_new<0 or y_new>=m: continue
            if field[x_new][y_new]:
                stack.append((x_new,y_new))
                field[x_new][y_new]=False

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