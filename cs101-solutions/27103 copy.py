n,m=map(int,input().split())
*a,=map(int,input().split())
l=-1;minlength=1
while l+1<n:
    cur=set()
    while len(cur)<m and l+1<n:
        l+=1; cur.add(a[l])
    if len(cur)==m: minlength+=1
print(minlength)
#划分成一系列组，每组保证有1-m的全部，总组数+1=最短所需长度