for _ in range(0,int(input())):
    n=int(input())
    a_b=[]
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    for index in range(0,n): a_b.append([A[index],B[index]])
    a_b.sort(key=lambda x:x[0])
    sum_time_min=cost=sum(B)
    for i in range(0,n):
        if a_b[i][0]>a_b[i-1][0]: sum_time_min=min(sum_time_min,max(a_b[i-1][0],cost))
        cost-=a_b[i][1]
    sum_time_min=min(sum_time_min,max(a_b[n-1][0],cost))
    print(sum_time_min)