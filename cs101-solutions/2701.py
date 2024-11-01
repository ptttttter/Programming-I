def judge(m):
    if m%7==0 or m%10==7 or m//10==7:
        return True
    else:
        return False
n=int(input())
sum=0
for i in range(1,n+1):
    if judge(i)==False:
        sum+=i**2
print(sum)