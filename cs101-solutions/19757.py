def exist(l,r,lst):
    left_index=0
    right_index=len(lst)-1
    while left_index<right_index:
        mid_index=(left_index+right_index)//2
        if l<=lst[mid_index]<=r:
            return True
        elif lst[mid_index]<l:
            left_index=mid_index+1
        else:
            right_index=mid_index-1
    return l<=lst[left_index]<=r
while True:
    R,n=map(int,input().split())
    if n==-1: break
    x=list(map(int,input().split()))
    x.sort()
    i=0;ct=n
    left=x[0]-R;right=x[0]+R
    lst=[x[0]]
    for i in range(1,n):
        joined=False
        if x[i]+R>=left and x[i]-R<=right:
            left=max(left,x[i]-R)
            right=min(right,x[i]+R)
            lst.append(x[i])
            if exist(left,right,lst):
                ct-=1
                joined=True
        if not(joined): 
            left,right=x[i]-R,x[i]+R
            lst=[x[i]]
    print(ct)