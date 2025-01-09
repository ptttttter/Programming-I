def main():
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    if sum(a)%x!=0: return n
    #left
    i=0
    while i<n and a[i]%x==0:
        i+=1
    if i==n: return -1
    j=0
    while j<n and a[n-1-j]%x==0:
        j+=1
    return n-min(i,j)-1
for _ in range(0,int(input())):
    print(main())