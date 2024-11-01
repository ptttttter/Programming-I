while True:
    n,m=map(int,input().split())
    if n==0 and m==0: break
    rest=n
    state=[True for _ in range(0,n+1)]
    num=1
    point=1
    while rest>=1:
        point+=1
        if point==n+1: point=1
        if state[point]==False: continue
        if rest==1:
            print(point)
            break
        num+=1
        if num==m:
            num=0
            rest-=1
            state[point]=False