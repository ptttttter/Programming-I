T=int(input())
for _ in range(0,T):
    N=int(input())
    ct=0
    turn=True
    while N>=1:
        if N%2==0:
            N=N//2
            ct+=N*turn
        else:
            N-=1
            ct+=turn
        turn=not(turn)
    print(ct)