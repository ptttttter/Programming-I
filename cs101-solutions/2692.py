T=int(input())
for _ in range(0,T):
    state=[0 for i in range(0,12)]
    #0 unknown 1 average 2 possibly heavy 3 possibly light
    for i in range(0,3):
        left,right,compare=[str for str in input().split()]
        l_num=[ord(s)-ord('A') for s in left]
        r_num=[ord(s)-ord('A') for s in right]
        if compare=="even":
            for i in l_num:
                state[i]=1
            for i in r_num:
                state[i]=1
        else:
            if compare=="up":
                a,b=2,3
            else:
                a,b=3,2
            for i in l_num:
                if state[i]==0:
                    state[i]=a
                elif state[i]==b:
                    state[i]=1
            for i in r_num:
                if state[i]==0:
                    state[i]=b
                elif state[i]==a:
                    state[i]=1
            for i in range(0,12):
                if (i not in l_num) and (i not in r_num):
                    state[i]=1
    for j in range(0,12):
        if state[j]==2:
            print("%s is the counterfeit coin and it is heavy." % chr(j+ord('A')))
            break
        if state[j]==3:
            print("%s is the counterfeit coin and it is light." % chr(j+ord('A')))
            break