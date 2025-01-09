t=int(input())
for _ in range(t):
    n=int(input())
    judge=True
    while n>=2:
        if n%2==0:
            n=n//2
        else:
            judge=False
            break
    if judge==True:
        print("NO")
    else:
        print("YES")