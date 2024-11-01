for _ in range(0,int(input())):
    x=int(input())
    length=0
    k=0;l_k=0
    while length<x:
        k+=1
        l_k+=len(str(k))
        length+=l_k
    length-=l_k
    num=0;num_digit=0
    for i in range(0,x-length):
        num_digit+=1
        if num_digit==len(str(num)):
            num+=1
            num_digit=0
    print(str(num)[num_digit])
