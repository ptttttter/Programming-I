while True:
    try:
        n=int(input())
        *b,=map(int,input().split())
    except EOFError:
        break
    time=sum(b)-max(b) if max(b)*2>sum(b) else sum(b)/2
    print("%.1f"%time)