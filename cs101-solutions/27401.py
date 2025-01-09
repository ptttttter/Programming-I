n,t=map(int,input().split())
*p,=map(int,input().split())
if t>sum(p):
    print(0)
else:
    sum_price={0}
    for i in range(0,n):
        sum_price_copy=sum_price.copy()
        for s in sum_price_copy:
            sum_price.add(s+p[i])
    g=t
    while g not in sum_price:
        g+=1
    print(g)