#binary search
import bisect
T=int(input())
a=list(map(int,input().split()))
a.sort()
l=a[0]+a[1];r=a[-1]+a[-2]
for index in range(0,len(a)):
    i=a[index]
    index_l=bisect.bisect_left(a,T-i)
    index_r=bisect.bisect_right(a,T-i)
    if index==index_l: index_l+=1;d=2
    else: d=1
    if index==index_r: index_r+=1

    if index_l==index_r:
        if index_l!=0: l=max(l,i+a[index_l-d])
        if index_r!=len(a): r=min(r,i+a[index_r])
    else:
        l=r=T
        break
print(l if T-l<=r-T else r)