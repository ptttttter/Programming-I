import math
n,m=[int(i) for i in input().split()]
rest=n
day=0
while rest>0:
    rest-=1
    day+=1
    if day%m==0:
        rest+=1
print(day)