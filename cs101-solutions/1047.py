def cyclic(str):
    num=int(str);n=len(str)
    cover=[0]*n
    for i in range(1,n+1):
        str_cyc=str[i:]+str[:i]
        if int(str_cyc)%num==0:
            p=int(str_cyc)//num
            if p<=n:
                cover[p-1]=1
    return bool(min(cover))
while True:
    try:
        str=input()
        if cyclic(str):
            print(f"{str} is cyclic")
        else:
            print(f"{str} is not cyclic")
    except EOFError:
        break
