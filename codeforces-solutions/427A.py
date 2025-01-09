n=int(input())
A=[int(i) for i in input().split()]
crime=0
police=0
for i in range(0,n):
    if A[i]==-1:
        if police>0:
            police-=1
        else:
            crime+=1
    else:
        police=police+A[i]
print(crime)
