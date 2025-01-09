n,m=map(int,input().split())
a=list(map(int,input().split()))
l=[]
for _ in range(0,m):
    l.append(int(input()))
lst=set()
ct=[0]*(n+1)
for j in range(n-1,-1,-1):
    if a[j] in lst:
        ct[j]=ct[j+1]
    else:
        ct[j]=ct[j+1]+1
        lst.add(a[j])
for l_i in l:
    print(ct[l_i-1])