n,m=map(int,input().split())
plans=[]
for i in range(0,n):
    x,y=map(int,input().split())
    for st in range(max(0,x+1-y),min(m-y,x)+1):
        plans.append((st,st+y))
plans.sort(key=lambda p:p[1])
left=0; cnt=0
for i in range(0,len(plans)):
    if plans[i][0]>=left:
        left=plans[i][1]
        cnt+=1
print(cnt)
#生成开发商所有修建方案，然后greedy数区间。x[i]必须取到保证了生成所有方案不会导致多数。