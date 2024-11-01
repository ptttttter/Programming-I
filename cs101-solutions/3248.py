while True:
    try:
        a,b=map(int,input().split())
        while(a!=b):
            a,b=min(a,b),max(a,b)
            b=b-a
        print(a)
    except EOFError:
        break