line=input()
line_out=""
for s in line:
    #65-90 A-Z
    #97-122 a-z
    i=ord(s)
    if i>=65 and i<=90:
        s_out=chr(i+32)
    elif i>=97 and i<=122:
        s_out=chr(i-32)
    else:
        s_out=s
    line_out+=s_out
print(line_out)