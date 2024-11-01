#n^2 brute force
T=int(input())
a=list(map(int,input().split()))
a.sort()
near_l=a[0]
near_r=a[-1]+a[-2]
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if j==i: continue
        if a[i]+a[j]<T:
            near_l=max(near_l,a[i]+a[j])
        else:
            near_r=min(near_r,a[i]+a[j])
if near_r-T>=T-near_l:
    print(near_l)
else:
    print(near_r)