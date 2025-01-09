n=int(input())
x=list(map(int,input().split()))
x.sort()
for _ in range(0,int(input())):
    m=int(input())
    l=0;r=n
    while l<r:
        mid=(l+r)//2
        if x[mid]>m:
            r=mid
        else:
            l=mid+1
    print(l)