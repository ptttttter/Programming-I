def factor(n,p):
    ct=0
    while n%p==0:
        n=n//p
        ct+=1
    return ct
def pow2(n):
    while n%2==0:
        n=n//2
    if n==1: return True
    else: return False
for _ in range(0,int(input())):
    n,m=map(int,input().split())
    delta=factor(n,3)-factor(m,3)
    m=m*(3**delta)
    if m%n==0 and pow2(m//n) and factor(m//n,2)<=delta:
        print("YES")
    else:
        print("NO")