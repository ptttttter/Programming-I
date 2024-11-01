for _ in range(0,int(input())):
    n=int(input())
    s=[0]*n;d=[0]*n
    test=[]
    ct=0
    for i in range(0,n):
        s[i],d[i]=map(int,input().split())
        update=False
        for j in range(0,ct):
            if test[j][0]<=d[i] and s[i]<=test[j][1]:
                #update test[j]
                test[j][0]=max(test[j][0],s[i])
                test[j][1]=min(test[j][1],d[i])
                update=True
                break
        if update==False:
            test.append([s[i],d[i]])
            ct+=1
    print(ct)