import heapq
n=int(input())
*l,=map(int,input().split())
cost=0
heapq.heapify(l)
while len(l)>1:
    a=heapq.heappop(l)
    b=heapq.heappop(l)
    heapq.heappush(l,a+b)
    #huffman 合并最小两个
    cost+=(a+b)
print(cost)