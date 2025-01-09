from functools import cmp_to_key
def compare(a,b):
    if a[0]>b[0]:
        return 1
    elif a[0]<b[0]:
        return -1
    else:
        return b[1]-a[1]
for _ in range(0,int(input())):
    n,m,b=map(int,input().split())
    skill=[]
    for i in range(0,n):
        skill.append(list(map(int,input().split())))
    skill.sort(key=cmp_to_key(compare))
    harm_sum=0
    prev=0
    sk_used=0
    for i in range(0,n):
        if skill[i][0]>prev:
            prev=skill[i][0]
            harm_sum+=skill[i][1]
            sk_used=1
        else:
            if sk_used<m:
                harm_sum+=skill[i][1]
                sk_used+=1
            else:
                continue
        if harm_sum>=b:
            print(skill[i][0])
            break
    if harm_sum<b:
        print("alive")