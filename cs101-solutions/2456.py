n,c=map(int,input().split())
x=[]
for _ in range(n): x.append(int(input()))
x.sort()
def judge(k):
    cnt=1
    prev=x[0]
    for i in range(1,n):
        if x[i]-prev>=k:
            cnt+=1
            prev=x[i]
            if cnt>=c: return True
    return False
left=1
right=max(x)//(c-1)+1
while left<right:
    mid=(left+right+1)//2
    if judge(mid):
        left=mid
    else:
        right=mid-1
print(left)