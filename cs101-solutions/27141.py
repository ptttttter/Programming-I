n=int(input())
price=[int(p)-520 for p in input().split()]
prefixsum=[0]
for p in price:
    prefixsum.append(prefixsum[-1]+p)
from collections import defaultdict
dic=defaultdict(lambda :-1)
maxlength=0
for i in range(0,n+1):
    if dic[prefixsum[i]]==-1:
        dic[prefixsum[i]]=i
    else:
        maxlength=max(maxlength,i-dic[prefixsum[i]])
print(520*maxlength)