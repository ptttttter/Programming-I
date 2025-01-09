for _ in range(0,int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    cnt=0
    sum_set={0}
    prev=0
    for i in range(0,n):
        prev+=a[i]
        if prev in sum_set:
            cnt+=1
            sum_set={prev}
        else:
            sum_set.add(prev)
    print(cnt)