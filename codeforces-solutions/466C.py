import sys
n=int(input())
a=list(map(int,input().split()))
S=sum(a)
if n<3 or S%3!=0:
    print(0)
    sys.exit()
sum_value=[a[0]]*n #sum value of 0-i
j_count=[0]*n #how much numbers<=i can be j
ct=0
for j in range(1,n-1):
    sum_value[j]=sum_value[j-1]+a[j]
    if sum_value[j]==2*S//3: ct+=1
    j_count[j]=ct
ways=0
for i in range(0,n-2):
    if sum_value[i]==S//3: ways+=(ct-j_count[i])
print(ways)