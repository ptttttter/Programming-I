A=[int(i) for i in input().split()]
i,j,k,l=A
M=max(i,j,k,l)
for s in A:
    if s!=M:
        print(M-s,end=" ")