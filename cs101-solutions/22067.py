stack=[]
min_weight=[]
while True:
    try:
        operation=input()
        if operation[:3]=="min":
            if stack: print(min_weight[-1])
        elif operation[:3]=="pop":
            if stack: stack.pop(); min_weight.pop()
        else:
            stack.append(int(operation.split()[1]))
            if min_weight==[]:
                min_weight.append(stack[-1])
            else:
                min_weight.append(min(min_weight[-1],stack[-1]))
    except EOFError:
        break