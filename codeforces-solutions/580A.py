n=int(input())
a=list(map(int,input().split()))
pre=0
ct=0
l_max=0
for i in range(0,n):
    if a[i]>=pre:
        ct=ct+1
    else:
        l_max=max(l_max,ct)
        ct=1
    pre=a[i]
l_max=max(l_max,ct)
print(l_max)