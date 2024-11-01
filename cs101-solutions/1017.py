import math
def fill(boxs,rest):
    global a
    if a[1]<=boxs:
        a[0]=max(0,a[0]-(rest-4*a[1]))
        a[1]=0
    else:
        a[0]=max(0,a[0]-(rest-4*boxs))
        a[1]-=boxs
ans=[]
while True:
    a=list(map(int,input().split()))
    bags=0
    if a[0]+a[1]+a[2]+a[3]+a[4]+a[5]==0:
        break
    bags+=a[5] #pack 6*6
    a[5]=0
    bags+=a[4] 
    a[0]=max(0,a[0]-a[4]*11) 
    a[4]=0 #pack 5*5
    bags+=a[3]
    if a[1]<=a[3]*5:
        rest=4*(a[3]*5-a[1])
        a[1]=0
        a[0]=max(0,a[0]-rest)
    else:
        a[1]=a[1]-a[3]*5 
    a[3]=0 #pack 4*4
    bags+=math.ceil(a[2]/4)
    if a[2]%4==1: fill(5,27)
    if a[2]%4==2: fill(3,18)
    if a[2]%4==3: fill(1,9)
    a[2]=0 
    #pack 3*3
    bags+=math.ceil(a[1]/9)
    
    if a[1]%9!=0:
        a[0]=max(0,a[0]-4*(9-a[1]%9))
    a[1]=0 
    #pack 2*2
    bags+=math.ceil(a[0]/36)
    a[0]=0
    #pack 1*1
    ans.append(bags)
for ele in ans:
    print(ele)
