t=int(input())
for _ in range(t):
    n,k=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    A=[]
    for i in range(n):
        A.append((a[i],i))
    A.sort(key=lambda x:x[0])
    b.sort()
    output=[0 for _ in range(n)]
    for i in range(n): 
        output[A[i][1]]=b[i]
    for i in range(n):
        print(output[i],end=" ")
    print()