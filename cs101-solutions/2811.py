def generate():
    import collections
    stack=collections.deque()
    stack.append([])
    for i in range(0,6):
        for _ in range(0,len(stack)):
            method=stack.popleft()
            stack.extend([method+[0],method+[1]])
    return list(stack)
directions={(0,0),(0,1),(0,-1),(1,0),(-1,0)}
def update(op,line):
    global light_new
    for j in range(0,len(op)):
        if op[j]==1:
            for dx,dy in directions:
                x=line+dx; y=j+dy
                if 0<=x<5 and 0<=y<6:
                    light_new[x][y]=1-light_new[x][y]
light=[]
for _ in range(0,5):
    light.append(list(map(int,input().split())))
firstline=generate()
for op in firstline:
    operation=[[0]*6 for _ in range(5)]
    light_new=[]
    for i in range(0,5): light_new.append(light[i].copy())
    operation[0]=op
    update(op,0)
    for i in range(1,5):
        operation[i]=light_new[i-1].copy()
        update(light_new[i-1],i)
    if sum(light_new[4])==0:
        for op in operation:
            print(*op,sep=' ')
        break