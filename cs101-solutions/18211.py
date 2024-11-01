def sort_p(list):
    if len(list)==1: return list
    mid=(len(list)-1)//2
    L=sort_p(list[:mid+1])
    R=sort_p(list[mid+1:])
    j=0
    output=[]
    for i in range(0,mid+1):
        while j<len(R) and R[j]<L[i]:
            output.append(R[j])
            j+=1
        output.append(L[i])
    for i in range(j,len(R)): output.append(R[i])
    return output

money=int(input())
price=list(map(int,input().split()))
n=len(price)
price.sort()
i=0 #left pointer i
diff=0
for j in range(n-1,-1,-1): #right pointrt j
    while i<=j and money>=price[i]:
        money-=price[i]
        diff+=1
        i+=1
    if i>=j: break
    if diff>0:
        money+=price[j]
        diff-=1
print(diff)