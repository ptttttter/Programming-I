for _ in range(0,int(input())):
    n=int(input())
    s=[0 if x>2048 else x for x in map(int,input().split())]
    print({True:"YES",False:"NO"}[sum(s)>=2048])