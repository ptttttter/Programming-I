week=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
n=int(input())
for _ in range(n):
    ccyymmdd=input()
    c=int(ccyymmdd[0:2])
    y=int(ccyymmdd[2:4])
    m=int(ccyymmdd[4:6])
    d=int(ccyymmdd[6:8])
    if m==1 or m==2:
        m+=12
        y-=1
        if y==-1:
            y=99
            c-=1
    w=y+y//4+c//4-2*c+(26*(m+1))//10+d-1
    print(week[w%7])