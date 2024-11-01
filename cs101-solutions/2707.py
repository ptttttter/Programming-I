import math
n=int(input())
for _ in range(0,n):
    a,b,c=map(float,input().split())
    delta=b**2-4*a*c
    if delta>0:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        if a>0:
            print("x1=%.5f;x2=%.5f" % (x1,x2))
        else:
            print("x1=%.5f;x2=%.5f" % (x2,x1))
    elif delta==0:
        x1=-b/(2*a)
        print("x1=x2=%.5f" % x1)
    else:
        Re=-b/(2*a)
        if Re==0:
            Re=-Re
        Im=math.sqrt(-delta)/(2*abs(a))
        print("x1=%.5f+%.5fi;x2=%.5f-%.5fi"%(Re,Im,Re,Im))