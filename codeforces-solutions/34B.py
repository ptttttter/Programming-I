m,n=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
a.sort()
sum=0
for j in range(0,n):
    if a[j]>=0:
        break
    else:
        sum=sum-a[j]
print(sum)