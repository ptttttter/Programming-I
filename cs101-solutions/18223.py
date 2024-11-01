def cal(a,b,c,d,num):
    A=[]
    for _ in range(4):
        if num%2==0:
            A.append(-1)
        else:
            A.append(1)
        num=num//2
    return a*A[0]+b*A[1]+c*A[2]+d*A[3]

T=int(input())
for _ in range(T):
    a,b,c,d=[int(j) for j in input().split()]
    isable24=False
    for i in range(16):
        if cal(a,b,c,d,i)==24:
            isable24=True
            break
    if isable24==True:
        print("YES")
    else:
        print("NO")