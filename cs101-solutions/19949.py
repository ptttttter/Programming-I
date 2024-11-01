n=int(input())
ct=0
for _ in range(0,n):
    str=input()
    index=-1
    while True:
        index=str.find("###",index+1)
        if index==-1:
            break
        index=str.find("###",index+1)
        ct=ct+1
        while str[(index+4):(index+7)]=="###":
            index=str.find("###",index+1)
            index=str.find("###",index+1)
print(ct)