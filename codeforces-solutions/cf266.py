t=int(input())
for _ in range(0,t):
    a,b=[int(i) for i in input().split()]
    if a%b==0:
        print(0)
    else:
        print(b-a%b)