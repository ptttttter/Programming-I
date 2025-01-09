n=int(input())
*a,=map(int,input().split())
stack=[]
r=0
for i in range(0,n):
    x=i+1-a[i]; y=i+1+a[i]
    if y<=r: continue
    while stack and stack[-1][0]>=x:
        px,py=stack.pop()
        r=px-1
    if r+1<=n:
        stack.append((r+1,y))
        r=y
print(len(stack))