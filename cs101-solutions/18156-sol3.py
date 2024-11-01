#two pointers
T=int(input())
a=list(map(int,input().split()))
a.sort()
i=0;j=len(a)-1
l=0
while i<j:
    while i<j and a[i]+a[j]>T:
        j-=1
    if i==j: j+=1
    if a[i]+a[j]<=T: l=max(l,a[i]+a[j])
    i+=1
i=0;j=len(a)-1
r=a[-1]+a[-2]
while i<j:
    while i<j and a[i]+a[j]<T:
        i+=1
    if i==j: i-=1
    if a[i]+a[j]>=T: r=min(r,a[i]+a[j])
    j-=1
print(l if T-l<=r-T else r)