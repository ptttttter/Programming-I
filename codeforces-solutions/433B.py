n=int(input())
v=list(map(int,input().split()))
u=v.copy()
u.sort()
sum_v=[0 for i in range(0,n+1)]
sum_u=[0 for i in range(0,n+1)]
for i in range(1,n+1):
    sum_v[i]=sum_v[i-1]+v[i-1]
    sum_u[i]=sum_u[i-1]+u[i-1]
for _ in range(int(input())):
    type,l,r=map(int,input().split())
    if type==1:
        print(sum_v[r]-sum_v[l-1])
    else:
        print(sum_u[r]-sum_u[l-1])