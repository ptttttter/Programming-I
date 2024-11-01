m,n,p,q=map(int,input().split())
matrix,core=[],[]
for _ in range(0,m): matrix.append(list(map(int,input().split())))
for _ in range(0,p): core.append(list(map(int,input().split())))

for i in range(m+1-p):
    for j in range(n+1-q):
        convolve_ij=0
        for k in range(p):
            for l in range(q):
                convolve_ij+=core[k][l]*matrix[i+k][j+l]
        print(convolve_ij,end=' ')
    print()