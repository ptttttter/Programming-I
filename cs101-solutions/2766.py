n=int(input())
matrix_list=[]
while True:
    try:
        matrix_list.extend(list(map(int,input().split())))
    except EOFError:
        break
matrix=[matrix_list[i*n:(i+1)*n] for i in range(0,n)]

sum=[[0]*(n+1) for _ in range(0,n+1)]

for i in range(1,n+1):
    line_sum=0
    for j in range(1,n+1):
        line_sum+=matrix[i-1][j-1]
        sum[i][j]=sum[i-1][j]+line_sum
sum_max_max=-128
for k in range(0,n):
    for j in range(k+1,n+1):
        i=1
        v=sum[i][j]+sum[i-1][k]-sum[i-1][j]-sum[i][k]
        prev=sum_max=v
        for i in range(2,n+1):
            v=sum[i][j]+sum[i-1][k]-sum[i-1][j]-sum[i][k]
            prev=max(v,v+prev)
            sum_max=max(sum_max,prev)
        sum_max_max=max(sum_max,sum_max_max)
print(sum_max_max)