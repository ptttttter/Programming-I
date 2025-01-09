import math
t=int(input())
for _ in range(0,t):
    m=int(input())
    k=0
    A=[]
    while m>=10:
        N=10**math.floor(math.log10(m))
        A.append((m//N)*N)
        m=m-(m//N)*N
        k=k+1
    if m>0:
        A.append(m)
        k=k+1
    print(k)
    for s in A:
        print(s,end=" ")
    print()
