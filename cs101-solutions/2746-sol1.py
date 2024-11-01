while True:
    n,m=map(int,input().split())
    if n==0 and m==0: break
    state=[True for _ in range(0,n+1)]
    point=1
    for i in range(1,n*m):
        while state[point]==False:
            point+=1
            if point>n: point=1
        if i%m==0:
            state[point]=False
        point+=1
        if point>n: point=1
    while state[point]==False:
        point+=1
        if point>n: point=1
    print(point)