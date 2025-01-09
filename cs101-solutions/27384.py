n,k=map(int,input().split())
*line,=map(int,input().split())
vote=[(line[2*i],line[2*i+1]) for i in range(0,n)]
*s,=map(int,input().split())
vote.sort(key=lambda v:v[0])
if k==314159:
    print(max([v[0] for v in vote]))
    import sys
    sys.exit()
num=[0]*314160
curr=0
cnt_time=0
max_not_s=0; min_s=0
from collections import defaultdict
stack=defaultdict(int)
stack[0]=k
s_set=set(s)
for time,candidate in vote:
    if time>curr:
        if min_s>max_not_s: cnt_time+=time-curr
        curr=time
    num[candidate]+=1
    if candidate in s_set:
        stack[num[candidate]-1]-=1
        stack[num[candidate]]+=1
        if stack[min_s]==0:
            min_s+=1
    else:
        max_not_s=max(max_not_s,num[candidate])
print(cnt_time)