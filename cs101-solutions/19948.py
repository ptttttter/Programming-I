n,m=map(int,input().split())
r=list(map(int,input().split()))
r.sort()
dis=[]
for i in range(1,n):
    dis.append(r[i]-r[i-1])
dis.sort(reverse=True)
print(sum(dis[m-1:]))