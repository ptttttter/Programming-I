l,n,m=map(int,input().split())
rocks=[]
for i in range(0,n):
    rocks.append(int(input()))
def judge(k):
    prev=0
    remove=0
    for i in range(0,len(rocks)):
        if rocks[i]-prev>=k and l-rocks[i]>=k:
            prev=rocks[i]
        else:
            remove+=1
            if remove>m: return False
    return bool(l>=k)
left=1
right=l//(n-m+1)+1
while left<right:
    mid=(left+right)//2+1
    if judge(mid):
        left=mid
    else:
        right=mid-1
print(left)