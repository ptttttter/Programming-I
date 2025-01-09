str=input()
judge=True
index=-1
for s in "hello":
    index=str.find(s,index+1,str.__len__())
    if index==-1:
        print("NO")
        judge=False
        break
if judge:
    print("YES")