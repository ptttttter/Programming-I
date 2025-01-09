for _ in range(0,int(input())):
    n=int(input())
    s=[bool(int(l)) for l in input()]
    
    ct_0=0
    position_0=[-1]*(n)
    for i in range(0,n):
        if not(s[i]):
            ct_0+=1
            position_0[ct_0]=i

    discount_money=0
    ed=0
    for i in range(n-1,-1,-1):
        if not(s[i]): continue
        discnt=False
        while ct_0>0:
            if position_0[ct_0]<i:
                discnt=True
                ct_0-=1
                break
            else:
                ct_0-=1
        if discnt:
            discount_money+=(i+1)
            continue
        else:
            ed=i
            break
    st=0
    while ed>st:
        while ed>=0 and s[ed]==0:
            ed-=1
        while st<n and s[st]==0:
            st+=1
        if ed>st:
            discount_money+=(ed+1)
        ed-=1
        st+=1
    print(n*(n+1)//2-discount_money)