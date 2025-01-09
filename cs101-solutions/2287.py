from bisect import bisect_left,bisect_right
ans=[]
while True:
    n=int(input())
    if n==0: break
    mine=[]
    while len(mine)<n: mine.extend(list(map(int,input().split())))
    adversary=[]
    while len(adversary)<n: adversary.extend(list(map(int,input().split())))

    mine.sort(); adversary.sort()
    
    win=0; lose=0
    i=0; j=n-1
    while i<=j:
        r=0
        while r<len(adversary):
            index=bisect_left(adversary,mine[i])
            r=(index-1)%len(adversary)
            if index==0:
                if mine[i]==adversary[0]: break
                lose+=(int)(mine[i]<adversary[-1])
            else:
                win+=1
            del adversary[r]
            i+=1
        if adversary==[]: break
        index=bisect_left(adversary,mine[j])
        r=(index-1)%len(adversary)
        if index==0:
            if mine[i]==adversary[0]:
                win=win
                del adversary[0]
                continue
            else:
                lose+=(int)(mine[j]<adversary[-1])
        else:
            win+=1
        del adversary[r]
        j-=1
    ans.append(200*(win-lose))
print(*ans,sep='\n')