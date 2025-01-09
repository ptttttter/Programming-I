import math
n=int(input())
input_list=map(int,input().split())
p=[True for _ in range(0,1000001)]
p[0]=0
p[1]=0
for i in range(2,1001):
    if p[i]==0: continue
    for j in range(2*i,1000001,i):
        p[j]=0
for item in input_list:
    sqrt_item=int(math.sqrt(item))
    if sqrt_item**2!=item:
        print("NO")
    else:
        if p[sqrt_item]:
            print("YES")
        else:
            print("NO")