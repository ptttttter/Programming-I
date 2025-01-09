import heapq
n,k=map(int,input().split())
*nums,=map(int,input().split())
ans=[]
q=[]
for i in range(0,k):
    heapq.heappush(q,(-nums[i],i))
ans.append(-q[0][0])
for i in range(k,n):
    heapq.heappush(q,(-nums[i],i))
    while q[0][1]<=i-k:
        heapq.heappop(q)
    ans.append(-q[0][0])
print(*ans,sep=' ')