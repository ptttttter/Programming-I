m,n=map(int,input().split())
pos=[]
for i in range(0,m):
    pos.append(list(map(int,input().split())))
answer=[]
scores=[]
for _ in range(0,n*m):
    answer.append(input())
    scores.append(answer[_].count('1'))
copycnt=0
for i in range(0,m):
    for j in range(0,n):
        index=pos[i][j]
        directions={(1,0),(-1,0),(0,1),(0,-1)}
        judge=False
        for dx,dy in directions:
            if 0<=i+dx<m and 0<=j+dy<n:
                if answer[index]==answer[pos[i+dx][j+dy]]:
                    judge=True
        if judge:
            copycnt+=1
scores.sort()
import math,bisect
index=math.ceil(0.6*m*n)-1
indexnew=bisect.bisect_left(scores,scores[index]+1)
print(copycnt,m*n-indexnew)