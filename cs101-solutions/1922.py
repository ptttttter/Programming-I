import math
while True:
    n=int(input())
    if n==0:
        break
    t_min=100000
    for _ in range(0,n):
        v,t=map(int,input().split())
        if t<0:
            continue
        t_arrive=math.ceil(t+4.5*3600/v)
        t_min=min(t_min,t_arrive)
    print(t_min)