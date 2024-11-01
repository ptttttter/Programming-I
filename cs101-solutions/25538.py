n=int(input())
n_2=str(bin(n))
s=n_2[2:]
judge=True
L=s.__len__()
for i in range(0,L):
    if s[i]!=s[L-1-i]:
        judge=False
if judge:
    print("Yes")
else:
    print("No")