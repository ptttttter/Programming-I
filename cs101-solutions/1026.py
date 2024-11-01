def encode(string,cipher,period,k):
    l=len(string)
    str_encode=['']*l
    for i in range(0,l):
        coordinate=i
        for _ in range(0,k%period[i]):
            coordinate=cipher[coordinate]-1
        str_encode[coordinate]=string[i]
    return ''.join(str_encode)
while True:
    n=int(input())
    if n==0: break
    a=list(map(int,input().split()))
    period_list=[0]*n
    for i in range(0,n):
        j=a[i]-1
        ct=1
        while j!=i:
            j=a[j]-1
            ct+=1
        period_list[i]=ct
    while True:
        s=input()
        if s=="0":break
        index=s.find(' ')
        k=int(s[:index])
        s=s[index+1:].ljust(n,' ')
        print(encode(s,a,period_list,k))
    print()
print()
