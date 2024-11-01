def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
x=int(input())
if x<6 or x%2==1:
    print("Error!")
else:
    for j in range(2,x//2+1):
        if prime(j) and prime(x-j):
            print("%d=%d+%d" % (x,j,x-j))