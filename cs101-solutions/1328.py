import math
T=0
while True:
    T+=1
    n,d=map(int,input().split())
    if n==0: break
    radar=[]
    island=[]
    possible=True
    for _ in range(0,n):
        x,y=map(int,input().split())
        if y>d: possible=False
        island.append((x,y))
    input()
    if not(possible): print(f"Case {T}: -1");continue
    island.sort(key=lambda t:t[0]+math.sqrt(d**2-t[1]**2))
    for x,y in island:
        left=x-math.sqrt(d**2-y**2)
        right=x+math.sqrt(d**2-y**2)
        update=False
        for i in range(0,len(radar)):
            if left<=radar[i][1] and right>=radar[i][0]:
                radar[i][0]=max(left,radar[i][0])
                radar[i][1]=min(right,radar[i][1])
                update=True
                break
        if not(update): radar.append([left,right])
    print(f"Case {T}: %d"%len(radar))