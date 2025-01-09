n,l=map(int,input().split())
A=list(map(int,input().split()))
A.append(0);A.append(l)
A.sort()
max_dis=0
for i in range(1,len(A)):
    d=A[i]-A[i-1]
    if i==1 or i==len(A)-1:
        d*=2
    max_dis=max(d,max_dis)
print("%.10f"% (max_dis/2))