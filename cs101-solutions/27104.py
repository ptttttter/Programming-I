n=int(input())
*a,=map(int,input().split())
lst=[(i-a[i-1],i+a[i-1]) for i in range(1,n+1)]
lst.sort()

i=0
target=1
cnt=1
right_boundary=0
while i<n:
    if lst[i][0]<=target:
        right_boundary=max(right_boundary,lst[i][1])
    else:
        target=right_boundary+1
        if target<=n: cnt+=1
    i+=1
print(cnt)
#与雷达安装区别：摄像头放在不同位置半径不同