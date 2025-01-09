def inverse_order(a):
    if len(a)==1: return 0
    mid=len(a)//2
    left=a[:mid]; right=a[mid:]
    inter_inverse=0
    i=0; j=0
    inner_inverse=inverse_order(left)+inverse_order(right)
    left.sort(); right.sort()
    while i<mid:
        while j<len(right) and right[j]<left[i]:
            j=j+1
            inter_inverse+=(mid-i)
        i=i+1
    return inter_inverse+inner_inverse
n=int(input())
*lst,=map(int,input().split())
print(inverse_order(lst))