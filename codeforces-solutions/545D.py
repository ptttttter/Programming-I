n=int(input())
t=list(map(int,input().split()))
t.sort()
ct=0
sum_time=0
for i in range(0,n):
    if t[i]>=sum_time:
        ct+=1
        sum_time+=t[i]
print(ct)