str=input()
pre=str[0]
ct=1
danger=False
for s in str[1:]:
    if s==pre:
        ct+=1
    else:
        pre=s
        ct=1
    if ct>=7:
        danger=True
        break
if danger==True:
    print("YES")
else:
    print("NO")