def length(n):
    if n==1:
        return 0.50
    else:
        return length(n-1)+1/(n+1)
while True:
    l=float(input())
    if l==0.00:
        break
    for i in range(1,277):
        if length(i)>l:
            print(i,"card(s)")
            break