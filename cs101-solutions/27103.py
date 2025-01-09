def minLength(lst:list[int],m):
    if len(lst)<m: return 1
    lmin=len(lst)+1
    for i in range(0,m):
        if i not in lst:
            return 1
        else:
            index=lst.index(i)
            lmin=min(lmin,minLength(lst[index+1:],i))
    return lmin+1
n,m=map(int,input().split())
*a,=map(int,input().split())
print(minLength(a,m))