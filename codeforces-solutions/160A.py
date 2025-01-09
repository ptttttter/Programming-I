n=int(input())
a=[int(i) for i in input().split()]
a.sort(reverse=True)
sum=0
for v in a:
    sum=sum+v
value_1=0
ct=0
for v in a:
    value_1+=v
    ct+=1
    if 2*value_1>sum:
        break
print(ct)