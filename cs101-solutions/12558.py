def length(land,i_st,j_st):
    i=i_st+1; j=j_st
    len_island=1
    while (i,j)!=(i_st,j_st):
        len_island+=1
        if land[i][j] and not(land[i][j-1]):
            i+=1 #向下移动
        elif land[i-1][j] and not(land[i][j]):
            j+=1 #向右移动
        elif land[i-1][j-1] and not(land[i-1][j]):
            i-=1 #向上移动
        elif land[i][j-1] and not(land[i-1][j-1]):
            j-=1 #向左移动
    return len_island
def solve():
    n,m=map(int,input().split())
    land=[[0] for _ in range(n+2)]
    land[0]=[0]*(m+2)
    for _ in range(1,n+1):
        land[_].extend(list(map(int,input().split())))
        land[_].append(0)
    land[n+1]=[0]*(m+2)
    for i in range(0,n+2):
        for j in range(0,m+2):
            if land[i][j]==1:
                return length(land,i,j)
print(solve())