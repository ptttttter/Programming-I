#实际在求递增子序列的最少数量
from bisect import bisect_left
for _ in range(0,int(input())):
    n=int(input())
    input_list=list(map(int,input().split()))
    l=input_list[0::2]
    w=input_list[1::2]
    stick=[(l[i],w[i]) for i in range(0,n)]
    stick.sort(key=lambda x:x[0])

    stick.reverse()
    record=[] #用record来存储最长上升子序列中每个元素所在下降子序列的最小元素
    for i in range(0,n):
        p=stick[i][1]
        index=bisect_left(record,p)
        if index==len(record):
            record.append(p)
        else:
            record[index]=p
    print(len(record))