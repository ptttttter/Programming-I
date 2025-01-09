n=int(input())
A=list(map(int,input().split()))
max_ct=1
for a in A:
    max_ct=max(max_ct,A.count(a))
print(max_ct)