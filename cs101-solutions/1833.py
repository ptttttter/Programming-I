import bisect
def update(a:list[int]):
    prev=a[0]
    i=1
    while i<len(a) and a[i]>prev:
        prev=a[i]
        i+=1
    if i==len(a): return list(reversed(a))
    index=bisect.bisect_left(a[:i],a[i])
    a_update=a[i-1::-1]+a[i:]
    a_update[i]=a[index];a_update[i-1-index]=a[i]
    return a_update
m=int(input())
for _ in range(0,m):
    n,k=map(int,input().split())
    array=list(map(int,input().split()))
    array.reverse()
    for i in range(0,k):
        array=update(array)
    array.reverse()
    print(*array,sep=' ')