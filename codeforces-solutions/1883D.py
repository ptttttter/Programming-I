q=int(input())
from collections import defaultdict
import heapq
leftpoint=defaultdict(int)
rightpoint=defaultdict(int)
heap_l=[]
heap_r=[]
for _ in range(0,q):
    s,l,r=input().split()
    l,r=int(l),int(r)
    if s=="+":
        leftpoint[l]+=1
        rightpoint[r]+=1
        heapq.heappush(heap_l,-l)
        heapq.heappush(heap_r,r)
    else:
        leftpoint[l]-=1
        rightpoint[r]-=1
    min_r=1E9+5; max_l=-1
    while heap_r:
        min_r=heap_r[0]
        if rightpoint[min_r]>0: break
        else: heapq.heappop(heap_r)
    while heap_l:
        max_l=-heap_l[0]
        if leftpoint[max_l]>0: break
        else: heapq.heappop(heap_l)
    if min_r<max_l:
        print("YES")
    else:
        print("NO")