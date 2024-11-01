n=int(input())
K=1000000
a=[0 for _ in range(0,K+1)]
a[1]=1
a[2]=2
for i in range(3,K+1):
    a[i]=2*a[i-1]+a[i-2]
    a[i]%=32767
for _ in range(0,n): print(a[int(input())])