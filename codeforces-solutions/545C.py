n=int(input())
x=[];h=[]
for _ in range(0,n):
    coord,height=map(int,input().split())
    x.append(coord);h.append(height)
ct=1;left=False #i=0
for i in range(1,n):
    distance=x[i]-x[i-1]-h[i-1]*int(left)
    left=False
    if distance>h[i]:
        ct+=1
    else:
        if i==n-1 or x[i+1]-x[i]>h[i]:
            left=True
            ct+=1
print(ct)