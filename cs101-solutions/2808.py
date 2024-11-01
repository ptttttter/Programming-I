L,M=[int(i) for i in input().split()]
tree=[True for _ in range(0,L+1)]
for _ in range(0,M):
    l,r=[int(i) for i in input().split()]
    for j in range(l,r+1):
        tree[j]=False
ct=0
for i in range(0,L+1):
    if tree[i]:
        ct=ct+1
print(ct)