t,k=map(int,input().split())
p=1000000007
up_lim=100000
ans=[0]*(up_lim+1); ans[0]=1
sum_ans=[0]*(up_lim+1)
for x in range(1,up_lim+1):
    if x>=k: ans[x]=ans[x-1]+ans[x-k]
    else: ans[x]=ans[x-1]
    ans[x]%=p
    sum_ans[x]=sum_ans[x-1]+ans[x] 
    sum_ans[x]%=p
for _ in range(0,t):
    a,b=map(int,input().split())
    print((sum_ans[b]-sum_ans[a-1])%p)