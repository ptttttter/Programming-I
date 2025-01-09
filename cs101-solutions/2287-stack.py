mine=[];abversary=[]
n=0
def count_win(match,i):
    cnt=0
    for index in range(0,i+1):
        if mine[index]>adversary[match[index]]:
            cnt+=1
        elif mine[index]<adversary[match[index]]:
            cnt-=1
    return cnt
def dfs():
    stack=[(-1,-1)]
    match=[-1]*n
    max_victory=-n
    while stack:
        i,j=stack.pop() #我的i - 对手的j
        if i>=0: match[i]=j
        if i+1==n:
            max_victory=max(max_victory,count_win(match,i))
            continue
        record=[False]*n
        for index in range(0,i+1):
            record[match[index]]=True

        h=mine[i+1] #为第i+1匹马分配对手
        st=0
        while record[st]: st+=1
        if h>adversary[st]:
            prev=k=st
            while k<n and adversary[k]<h:
                if not(record[k]): prev=k
                k+=1
            ad=[prev]
        else:
            ed=n-1
            while record[ed]: ed-=1
            ad=[ed]
            if h==adversary[st]: ad.append(st)
        for item in ad:
            stack.append((i+1,item))
    return max_victory
        
while True:
    n=int(input())
    if n==0: break
    *mine,=map(int,input().split())
    *adversary,=map(int,input().split())
    mine.sort(); adversary.sort()
    print(200*dfs())