n=int(input())
T=list(map(int,input().split()))
A=[[T[i],i] for i in range(0,n)]
A.sort(key=lambda x:x[0])
sequence=[A[i][1]+1 for i in range(0,n)]
print(*sequence,sep=' ')
print("%.2f"%(sum([(n-1-i)*A[i][0] for i in range(0,n)])/n))