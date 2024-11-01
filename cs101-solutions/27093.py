N,D=map(int,input().split())
h=list(map(int,input().split()))

while h!=[]:
    max_h,min_h=h[0],h[0]
    group=[h[0]]
    others=[]
    for i in range(1,len(h)):
        max_h=max(max_h,h[i])
        min_h=min(min_h,h[i])
        if h[i]+D>=max_h and h[i]-D<=min_h:
            group.append(h[i])
        else:
            others.append(h[i])
    group.sort()
    h=others
    print(*group,sep=' ',end=' ')