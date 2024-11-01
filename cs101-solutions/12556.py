str=input().lower()
pre=str[0]
ct=1
for s in str[1:]:
    if s==pre:
        ct+=1
    else:
        print("(%s,%d)"%(pre,ct),end="")
        pre=s
        ct=1
print("(%s,%d)"%(pre,ct),end="")