row_A,col_A=map(int,input().split())
A=[]
for i in range(0,row_A):
    A.append(list(map(int,input().split())))
row_B,col_B=map(int,input().split())
B=[]
for i in range(0,row_B):
    B.append(list(map(int,input().split())))
row_C,col_C=map(int,input().split())
C=[]
for i in range(0,row_C):
    C.append(list(map(int,input().split())))
if col_A==row_B and row_A==row_C and col_B==col_C:
    for i in range(0,row_C):
        for j in range(0,col_C):
            for k in range(0,col_A):
                C[i][j]+=A[i][k]*B[k][j]
            print(C[i][j],end=" ")
        print()
else:
    print("Error!")