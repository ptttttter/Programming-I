n=int(input())
for _ in range(0,n):
    s=int(input())
    a=int(input())
    A=list(map(int,input().split()))
    b=int(input())
    B=list(map(int,input().split()))
    ct=0
    count_B=[0 for i in range(0,10001)]
    for q in B:
        count_B[q]+=1
    for p in A:
        if s<=p: continue
        ct+=count_B[s-p]
    print(ct)