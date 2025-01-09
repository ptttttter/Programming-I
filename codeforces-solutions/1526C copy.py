class Heap:
    def __init__(self):
        self.heap=[]
    def length(self):
        return len(self.heap)
    def heappop(self):
        top=self.heap[0]
        end=self.heap.pop()
        if self.heap==[]:
            return top
        self.heap[0]=end
        n=len(self.heap)
        index=0        
        while 2*index+2<n:
            new_index=2*index+1 if self.heap[2*index+1]<self.heap[2*index+2] else 2*index+2
            self.heap[index],self.heap[new_index]=self.heap[new_index],self.heap[index]
            index=new_index
        if 2*index+2==n and self.heap[index]>self.heap[2*index+1]:
            self.heap[index],self.heap[2*index+1]=self.heap[2*index+1],self.heap[index]
        return top
    def heappush(self,value):
        self.heap.append(value)
        index=self.length()-1
        while index>0:
            new_index=(index-1)>>1
            if self.heap[index]>=self.heap[new_index]:
                break
            else:
                self.heap[index],self.heap[new_index]=self.heap[new_index],self.heap[index]
            index=new_index
n=int(input())
*a,=map(int,input().split())
t=Heap()
cur=0
for p in a:
    cur+=p
    t.heappush(p)
    if cur<0:
        cur-=t.heappop()
print(t.length())