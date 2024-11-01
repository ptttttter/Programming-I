b=[0]*8 #b_0~b_7
chest=[[0]*8 for _ in range(0,8)]
methods=[]
def dfs(i,bi):
    global b,chest,methods
    b[i]=bi
    if i==7:
        methods.append("".join([str(position+1) for position in b]))
        return
    #update
    new=[[False]*8 for _ in range(0,8)]
    for j in range(i+1,8):
        for bj in [bi+K*(j-i) for K in [0,1,-1]]:
            if bj>=8 or bj<0: continue
            if chest[j][bj]==0: 
                chest[j][bj]=-1
                new[j][bj]=True
    #search
    for j in range(0,8):
        if chest[i+1][j]==0:
            dfs(i+1,j)
    #back
    for j in range(i+1,8):
        for bj in [bi+K*(j-i) for K in [0,1,-1]]:
            if bj>=8 or bj<0: continue
            if new[j][bj]: chest[j][bj]=0
for j in range(0,8):
    dfs(0,j)
for _ in range(0,int(input())):
    print(methods[int(input())-1])