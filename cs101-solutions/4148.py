test_no=0
while True:
    test_no+=1
    p,e,i,d=map(int,input().split())
    if p==-1: break
    f=(p+23*(p%4))//4
    g=(e+28*((3-e)%3))//3
    h=(i+33*(i%17))//17
    X=f*28*33+g*23*33+h*23*28
    day=(X-d)%21252
    if day==0: day=21252
    print(f"Case {test_no}: the next triple peak occurs in {day} days.")