import bisect
k=int(input())
a=list(map(int,input().split()))
#求序列a的最长递减子序列的长度->严格递增子序列的最少数量 (greedy)
#用in_seq=[] 记录严格递增子序列中的最大元素 
#in_seq是递减的，为了使用bisect我们取逆
a.reverse()
#求reversed(a)的严格递减子序列的最少数量
de_seq=[] #记录严格递减子序列中元素的最小值
for height in a:
    index=bisect.bisect_right(de_seq,height)
    if index==len(de_seq):
        de_seq.append(height)
    else:
        de_seq[index]=height
print(len(de_seq))