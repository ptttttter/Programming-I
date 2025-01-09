p=[True for i in range(0,10001)]
for i in range(2,100):
    if p[i]==False: continue
    for j in range(2*i,10001,i): p[j]=False
S=int(input())
if S%2==1:
    print(2*(S-2))
else:
    for i in range(S//2,3,-1):
        if p[i] and p[S-i]:
            print(i*(S-i))
            break