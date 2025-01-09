t=int(input())
for _ in range(0,t):
    n=int(input())
    #n=2**a*3**b*c
    a,b=0,0
    while n%2==0:
        n=n//2
        a=a+1
    while n%3==0:
        n=n//3
        b=b+1
    if n==1:
        if b>=a:
            print(2*b-a)
        else:
            print(-1)
    else:
        print(-1)