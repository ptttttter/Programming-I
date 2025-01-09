keyboard="qwertyuiopasdfghjkl;zxcvbnm,./"
I=input()
str=input()
out=""
if I=="R":
    d=1
else:
    d=-1
for s in str:
    out+=keyboard[keyboard.find(s)-d]
print(out)