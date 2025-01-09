operator=['+','-','*','/']
def calc(exp:list[str])->float:
    if len(exp)==1 and exp[0] not in operator:
        return float(exp[0])
    num_ct=0; oper_ct=0
    for i in range(1,len(exp)):
        if exp[i] in operator:
            oper_ct+=1
        else:
            num_ct+=1
        if num_ct==oper_ct+1:
            num_ct=0; oper_ct=0
            num_left=calc(exp[1:i+1])
            num_right=calc(exp[i+1:])
            break
    if exp[0]=='+':
        return num_left+num_right
    elif exp[0]=='-':
        return num_left-num_right
    elif exp[0]=='*':
        return num_left*num_right
    else: return num_left/num_right
expression=input().split()
print("%f"%calc(expression))