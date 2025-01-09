import math
t=int(input())
for _ in range(0,t):
    x,y,k=map(int,input().split())
    if k<=x and k<=y:
        print(f"0 0 {k} 0")
        print(f"0 0 0 {k}")
        continue
    if x<=y:
        y_D=math.ceil(math.sqrt(k**2-x**2))
        print(f"0 0 {y_D} {x}")
        print(f"{x} 0 0 {y_D}")
    else:
        x_D=math.ceil(math.sqrt(k**2-y**2))
        print(f"{x} 0 {x-x_D} {y}")
        print(f"0 0 {y} {x_D}")