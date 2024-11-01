d=int(input())
ct=[[0 for j in range(0,1025)] for i in range(0,1025)]
for _ in range(0,int(input())):
    x,y,num=map(int,input().split())
    for i in range(x-d,x+d+1):
        if i<0 or i>1024: continue
        for j in range(y-d,y+d+1):
            if j<0 or j>1024: continue
            ct[i][j]+=num
ct_max=-1
max_num=1
for i in range(0,1025):
    for j in range(0,1025):
        if ct[i][j]>ct_max:
            ct_max=ct[i][j]
            max_num=1
        elif ct[i][j]==ct_max:
            max_num+=1
print(max_num,ct_max)