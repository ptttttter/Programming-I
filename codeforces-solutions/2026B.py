def judge(a,k):
    i=0
    i_del=False
    while i<len(a)-1:
        if a[i+1]-a[i]>k:
            if i_del:
                return False
            else:
                i=i+1
                i_del=True
        else:
            i=i+2
    return True

t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    if n==1: print(1);continue
    if n%2==0:
        k=1
        for i in range(0,n,2):
            k=max(k,a[i+1]-a[i])
        print(k)
    else:
        left=1; right=a[n-1]-a[0]
        while left<right:
            mid=(left+right)//2
            if judge(a,mid):
                right=mid
            else:
                left=mid+1
        print(left)