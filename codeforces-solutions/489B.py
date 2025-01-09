n=int(input())
a=list(map(int,input().split()))
a.sort()
m=int(input())
b=list(map(int,input().split()))
b.sort()
s=[True for _ in range(0,m)]
ct=0
for i in range(0,n):
    for j in range(0,m):
        if s[j] and abs(b[j]-a[i])<=1:
            s[j]=False
            ct+=1
            break
print(ct)