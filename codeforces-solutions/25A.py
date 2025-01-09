n=int(input())
a=[int(i)%2 for i in input().split()]
if a.count(1)==1:
    search=1
else:
    search=0
for j in range(0,n):
    if a[j]==search:
        print(j+1)