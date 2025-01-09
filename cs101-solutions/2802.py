from collections import deque
def bfs(x1,x2,y1,y2,b,h,w):
    visited=[[False]*(h+2) for _ in range(0,w+2)]
    queue=deque()
    queue.append((x1,y1))
    visited[x1][y1]=True
    step=0
    while queue:
        for _ in range(len(queue)):
            x,y=queue.popleft()
            directions={(1,0),(-1,0),(0,1),(0,-1)}
            for dx,dy in directions:
                length=1
                while True:
                    x_next,y_next=x+length*dx,y+length*dy
                    if (x_next,y_next)==(x2,y2): return step+1
                    if x_next<0 or x_next>w+1 or y_next<0 or y_next>h+1 \
                        or visited[x_next][y_next] or b[x_next][y_next]==1: break
                    queue.append((x_next,y_next))
                    visited[x_next][y_next]=True
                    length+=1
        step+=1
    return -1
ans_board=[]
while True:
    w,h=map(int,input().split())
    if w==0: break
    ans=[]
    b=[[0]*(h+2) for _ in range(0,w+2)]
    for i in range(1,h+1):
        line=input()
        for j in range(1,w+1):
            if line[j-1]=='X': b[j][i]=1
    while True:
        x1,y1,x2,y2=map(int,input().split())
        if x1==0: break
        ans.append(bfs(x1,x2,y1,y2,b,h,w))
    ans_board.append(ans)
for i in range(len(ans_board)):
    print(f"Board #{i+1}:")
    for j in range(len(ans_board[i])):
        s=ans_board[i][j]
        if s==-1:
            print(f"Pair {j+1}: impossible.")
        else:
            print(f"Pair {j+1}: {s} segments.")
    print()