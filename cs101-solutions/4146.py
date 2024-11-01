n=int(input())
maximum=0
for a1 in range(0,n+1):
    for a2 in range(a1%2,n+1,2):
        inf=3-a2%3
        if inf==3: inf=0
        for a3 in range(inf,n+1,3):
            if (a1+a2+a3)%5==0: maximum=max(maximum,a1+a2+a3)
print(maximum)