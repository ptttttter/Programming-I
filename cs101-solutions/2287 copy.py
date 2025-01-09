def sgn(a):
    if a>0: return 1
    elif a<0: return -1
    else: return 0
ans=[]
while True:
    n=int(input())
    if n==0: break
    mine=[]
    while len(mine)<n: mine.extend(list(map(int,input().split())))
    adversary=[]
    while len(adversary)<n: adversary.extend(list(map(int,input().split())))

    mine.sort(); adversary.sort()
    max_win=-n
    for shift in range(0,n):
        win=0
        for i in range(0,n):
            win+=sgn(mine[(i+shift)%n]-adversary[i])
        max_win=max(max_win,win)
    ans.append(200*max_win)
print(*ans,sep='\n')