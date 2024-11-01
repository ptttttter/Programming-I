n=int(input())
words=[s for s in input().split()]
line=words[0]
for i in range(1,n):
    if len(line)+1+len(words[i])<=80:
        line=line+" "+words[i]
    else:
        print(line)
        line=words[i]
print(line)