from functools import cmp_to_key
def compare(s1,s2):
    if s2+s1<s1+s2: return 1
    else: return -1
m=int(input())
n=int(input())
*s,=input().split()
s.sort(key=cmp_to_key(compare),reverse=True)
dp=[0]*(m+1)
for i in range(1,n+1):
    for j in range(m,0,-1):
        if j-len(s[i-1])>=0:
           dp[j]=max(dp[j],int(str(dp[j-len(s[i-1])])+s[i-1]))
print(dp[m])