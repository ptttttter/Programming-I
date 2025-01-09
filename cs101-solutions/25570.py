n=int(input())
matrix=[]
for _ in range(n):
    *line,=map(int,input().split())
    matrix.append(line)
max_layer=0
for i in range((n+1)//2):
    layer=0
    for k in range(i+1,n-i):
        layer+=matrix[i][k]+matrix[k-1][i]+matrix[n-1-i][k-1]+matrix[k][n-1-i]
    if i*2==(n-1): layer=matrix[i][i]
    max_layer=max(max_layer,layer)
print(max_layer)