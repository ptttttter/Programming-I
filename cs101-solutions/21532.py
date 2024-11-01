import math
N=int(input())
record=False
for i in range(6,math.ceil(math.sqrt(N))+1):
    if N%i==0:
        print(N//i)
        record=True
        break
if record==False:
    for i in range(5,0,-1):
        if N%i==0 and N//i>=6:
            print(i)
            break