def judge(a,k):
    for i in range(0,k):
        if a[k-1+i]>i+1:
            return False
    return True
for _ in range(0,int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    left=0
    right=(n+1)//2
    while left<right:
        mid=(left+right+1)//2
        if judge(a,mid):
            left=mid
        else:
            right=mid-1
    print(left)