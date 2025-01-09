import math
n=int(input())
s=list(map(int,input().split()))
number=[s.count(i+1) for i in range(0,4)]
taxi=0
taxi+=number[3]+number[2]+number[1]//2
if number[1]%2==1: taxi+=1
if sum(s)<=taxi*4:
    print(taxi)
else:
    print(math.ceil(sum(s)/4))