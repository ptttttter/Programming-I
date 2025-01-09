import math
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(ai) for ai in input().split()]
    b=[int(bj) for bj in input().split()]
    sum_a,sum_b=0,0
    min_a,min_b=1e9,1e9
    for s in a:
        sum_a+=s
        min_a=min(min_a,s)
    for s in b:
        sum_b+=s
        min_b=min(min_b,s)
    cost=min(sum_a+n*min_b,sum_b+n*min_a)
    print("%d"%cost)